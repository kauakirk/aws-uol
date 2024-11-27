import csv

with open("csv.csv", mode='r') as arq:
    leitor = csv.reader(arq, delimiter=',')
    cont = 0
    for linha in leitor:
        if cont == 0:
            print(f"colunas {" ".join(linha)}")
            
