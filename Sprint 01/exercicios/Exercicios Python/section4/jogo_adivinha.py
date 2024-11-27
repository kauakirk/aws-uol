import random
import os

novo_jogo = 's'

while novo_jogo == 's':
    print('bem vindo ao jogo')
    print('voce tem 3 chances para adivinhar o numero entre 1 e 15: ')

    num = random.randint(1,15)

    for i in range(3):
        print("qual a sua escolha:  ")
        chute = int(input())

        if chute == num:
            print("voce acertou ")
            break
        elif chute> num:
            print('numero alto ')
        else:
         print('menor que o numero ')

    
    print("o numero segreto era o ", num)

    novo_jogo = input("quer jogar dnv? s ou n ")
    novo_jogo = novo_jogo.lower

    os.system('cls')

