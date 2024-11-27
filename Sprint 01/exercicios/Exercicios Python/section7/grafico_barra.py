import matplotlib.pyplot as plt

cidade_a = [70,31,32,33,34,35]
cidade_b = [32,35,36,33,34,22]
cidade_c = [10,41,22,53,14,35]

datas = [5,10,15,20,25,30]

posicoes_a = list(range(len(datas)))
posicoes_b = [pos + 0.8 for pos in posicoes_a]
posicoes_c = [pos + 0.8 for pos in posicoes_a]

plt.bar(posicoes_a, cidade_a, color='r', label='cidadeA')
plt.bar(posicoes_b, cidade_b, color='g', label='cidadeB')
plt.bar(posicoes_c, cidade_c, color='b', label='cidadeC')

plt.legend()

plt.xticks(ticks=posicoes_a, labels=datas)

plt.show()