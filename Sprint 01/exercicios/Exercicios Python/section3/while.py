# num = 1

# while(num <= 10):
#     print(num)
#     num += 1
# print('laco encerrado')

nome = None

while True:
    print('digite seu nome ou x para para: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print('bem vindo ', nome)