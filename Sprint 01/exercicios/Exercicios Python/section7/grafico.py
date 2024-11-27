from matplotlib  import pyplot as plt

# eixo_x_dias = [1,5,10,15,20,25,30]
# eixo_y_temp_max = [25,25,25,12,14,35,12]
# eixo_y_temp_min = [21,22,17,10,12,24,10]
# plt.title('temp max e min')
# plt.xlabel('datas')
# plt.ylabel('temp')

# plt.plot(eixo_x_dias, eixo_y_temp_max, label='Temp Max')
# plt.plot(eixo_x_dias, eixo_y_temp_min, label='Temp Min')

# plt.legend(loc='best')
#plt.axis([1,31,5, 45])
# plt.xlim([1,31])
# plt.ylim([-5,50])
# plt.grid(True)

#plt.savefig('Grafico.png')
#print(plt.style.available)

x = range(1,11,1)
plt.plot(x, [(val**3+1) for val in x])

plt.show()
