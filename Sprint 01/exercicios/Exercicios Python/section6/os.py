import os

os.chdir( "C:\\teste" )
print(f'diretorio atual: {os.getcwd()}')

padrao_nome = input("qual o padrao de nomes de arquivos a usar:  ")

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + '' + str(contador)

        nome_novo = f"{nome_arq}{exten_arq}"
        os.rename(arq, nome_novo)