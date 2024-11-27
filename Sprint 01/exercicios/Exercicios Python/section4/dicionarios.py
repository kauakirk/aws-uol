elemento = {
    'z': 3,
    'nome': 'litio',
    'grupo': 'Metais',
    'densidade': 0.534
}

print(elemento)

elemento = ['grupo'] = 'alcalinos'
print(elemento)

elemento['periodo'] = 1
print(elemento)

del elemento['periodo']
print(elemento)

elemento.clear()
del elemento

print(elemento.values())
