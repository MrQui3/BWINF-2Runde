import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


anzahl_array = [31, 61, 91, 121, 151, 181, 211, 241, 271, 301]
moves_array = [1374, 1143, 1078, 1065, 1067, 1065, 1064, 1063, 1063, 1063]
iterations_array = [1374, 9022, 17897, 24294, 29961, 34385, 38171, 41716, 45394, 51316]

plt.plot(anzahl_array, moves_array, marker='', linestyle='-', color='b')
plt.grid(True)
plt.xlabel('interationen l')
plt.ylabel('Anzahl an Schritten')
plt.show()
plt.plot(anzahl_array, iterations_array, marker='', linestyle='-', color='b')

plt.grid(True)
plt.xlabel('Begrenzung l')
plt.ylabel('Interationen')
plt.show()
