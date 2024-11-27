numeros = [1,2,3,6,35,63,23,53,23,64,65,35,2312]

# quadrados = [num**2 for num in numeros]
# print(quadrados)

# pares = [num for num in range(11) if num %2 ==0]
# print(pares)

frase = 'A logica eh apenas'
vogais = ['a', 'e', 'i', 'o', 'u']

lista_vogais = [v for v in frase if v in vogais]
print(lista_vogais)

distributiva = [k*m for k in[2,3,5] for m in [10,20,30]]
print(distributiva)

