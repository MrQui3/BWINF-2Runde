import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


anzahl_array = [1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 25,30, 35,40, 45, 50, 55, 65, 70, 75, 80, 85, 90, 95, 100]
moves_array = [5930, 3647, 2914, 2929, 4126, 2738, 2841, 2733, 2566, 2574, 2641, 2146, 2127, 2296, 2271, 2350, 2151, 2125, 2187, 2034, 2204, 2037, 2218, 2153, 2098]
iterations_array = [5930, 5792, 6423, 9611, 10815, 13065, 15546, 21176, 30359, 39217, 50845, 51589, 57383, 71794, 81137, 95203, 87549, 103736, 122761, 117867, 139066, 126027, 156986, 151542, 155364]


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
