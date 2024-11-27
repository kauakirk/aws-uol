# Simples, composto, encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))

media = (n1 + n2) / 2

if(media >= 7):
    print("Aprovado")
    
elif(media>=5):
    print("Recuperaçao")

else:
    print("Reprovado...")

print("Sua media é ", media)
