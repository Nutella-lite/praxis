import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=40)
plt.title('Гистограмма нормального распределения случайных чисел')
plt.show()

X = np.random.rand(100)
Y = np.random.rand(100)

plt.scatter(X, Y)
plt.title('Диаграмма рассеяния')
plt.xlabel('Координаты X')
plt.ylabel('Координаты Y')
plt.show()