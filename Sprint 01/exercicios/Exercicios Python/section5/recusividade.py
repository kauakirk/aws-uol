# recursividade

def fatorial(numero):
    if  numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1)


x = int(input("digite um numero"))
res = fatorial(x)

print(f"fatorial {res}")