n1 = int(input("digite numero: "))
n2 = int(input("digite numero: "))


try:
    r = round (n1 / n2, 2)
except ZeroDivisionError:
    print("imposivel dividir")
else:
    print(f'resultado: {r}')

def div(k,j):
    return round(k/j)