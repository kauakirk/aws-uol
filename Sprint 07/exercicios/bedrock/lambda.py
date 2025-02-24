import json
import boto3
import base64
import datetime

# Inicializando os clientes da AWS
client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Obtendo o prompt corretamente
    input_prompt = event.get('prompt') or event.get('queryStringParameters', {}).get('prompt', '')
    
    if not input_prompt:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing prompt parameter'})
        }
    
    print(f"Prompt recebido: {input_prompt}")

    # Chamando o Bedrock para gerar a imagem
    response_bedrock = client_bedrock.invoke_model(
        contentType='application/json',
        accept='application/json',
        modelId='amazon.titan-image-generator-v2:0',
        body=json.dumps({
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {
                "text": input_prompt
            },
            "imageGenerationConfig": {
                "quality": "standard",
                "numberOfImages": 1,
                "height": 512,
                "width": 512,
                "cfgScale": 7.5,
                "seed": 0       
            }
        })
    )

    # Lendo e decodificando a resposta do Bedrock
    response_bedrock_byte = json.loads(response_bedrock['body'].read())
    response_bedrock_base64 = response_bedrock_byte['images'][0]
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)

    # Criando um nome único para a imagem
    poster_name = 'poster_' + datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S') + '.png'

    # Enviando a imagem para o S3
    client_s3.put_object(
        Bucket='movieposterdes01',
        Body=response_bedrock_finalimage,
        Key=poster_name,
        ContentType='image/png'
    )

    # Gerando uma URL pré-assinada para acessar a imagem no S3
    presigned_url = client_s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': 'movieposterdes01', 'Key': poster_name},
        ExpiresIn=3600  # URL válida por 1 hora
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'image_url': presigned_url})
    }