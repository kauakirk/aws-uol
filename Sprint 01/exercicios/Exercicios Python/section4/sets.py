#set conjuntos

planeta_anao = {'Plutao', 'ceres', 'eris', 'haumea', 'makemake'}
print(len(planeta_anao))
print('ceres' in planeta_anao)
print('lua' in planeta_anao)

for astro in planeta_anao:
    print (astro.upper(), end='')

astros = ['lua', 'lua', 'lua', 'lua', 'lua', 'lua', 'marte', 'sirius']

astro_set = set(astros)
print(astro_set)