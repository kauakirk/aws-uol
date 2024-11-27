# quadrado = lambda x: x ** 2

# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0
# print(par(9))

# f_c = lambda f: (f-32)*5/9

# print(f_c(32))


# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavras = ['python', 'é', 'uma linggagem']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

# def numeros_pares(n):
#     return n % 2 == 0
# numeros = [1,2,3,6,35,63,23,53,23,64,65,35,2312]

# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

# numeros = [1,2,3,6,35,63,23,53,23,64,65,35,2312]
# num_impar = list(filter(lambda x: x%2 != 0, numeros))
# print(num_impar)

from functools import reduce

# def mult(x, y):
#     return x *y
# numeros = [1,2,3,6,35,63,23,53,23,64,65,35,2312]

# total = reduce(mult, numeros)
# print(total)
numeros = [1,2,3,6,35,63,23,53,23,64,65,35,2312]
total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)

