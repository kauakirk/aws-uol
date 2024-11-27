n1 = n2 = 0.0
faltas = 0

n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
faltas = int(input("digite as faltas: "))

media = (n1 + n2) / 2

if(faltas >= 10):
    print("Reprovado por faltao")

elif(media >= 7):
    print("Aprovado")
    
elif(media>=5):
    print("Recuperaçao")

else:
    print("Reprovado...")

print("Sua media é ", media)