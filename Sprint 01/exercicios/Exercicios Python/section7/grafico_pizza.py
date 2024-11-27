import matplotlib.pyplot as plt

linguagens = ['python', 'js', 'C', 'Ruby']

quantidades = [300, 270, 150, 40]

plt.pie(quantidades, labels=linguagens, autopct='%1.1f%%')
plt.title("Pref de Linguagens")
plt.legend(title='linguagens', loc='best')

plt.show