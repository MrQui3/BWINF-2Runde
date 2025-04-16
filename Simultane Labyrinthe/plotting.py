import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

anzahl_array = [1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 30, 40, 50, 60, 100]
moves_array = [19912, 16517, 16290, 15743, 15646, 15716, 15538, 15440, 15359, 15288, 15258, 15104, 15002, 15017, 14872]
iterations_array = [19912, 23673, 28579, 31526, 34801, 37340, 41943, 52652, 67819, 80367, 108535, 131407, 135790, 137445, 197173]

a = []
for i in range(len(anzahl_array)):
    a.append(anzahl_array[i]*(2*10200+10200))


plt.plot(anzahl_array, moves_array, marker='', linestyle='-', color='b')
plt.grid(True)
plt.xlabel('Begrenzung l')
plt.ylabel('Anzahl an Schritten')
plt.show()
plt.plot(anzahl_array, iterations_array, marker='', linestyle='-', color='b')
plt.plot(anzahl_array, a, marker='', linestyle='-', color='g')

plt.grid(True)
plt.xlabel('Begrenzung l')
plt.ylabel('Interationen')
plt.show()
