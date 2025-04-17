import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


anzahl_array = [1, 4, 5, 6, 7, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
moves_array = [5930, 2929, 4126, 2738, 2841, 2733, 2566, 2574, 2146, 2296, 2350, 2304, 2187, 2204, 2218, 2098, 1997, 1326, 2083, 1322, 1429, 1360, 1961, 1464, 1494, 1489, 2233, 1461, 1466, 1458, 1455, 1464, 1443, 1459, 1460, 1440]
iterations_array = [5930, 9611, 10815, 13065, 15546, 21176, 30359, 39217, 51589, 71794, 95203, 113312, 122761, 139066, 156986, 155364, 153683, 112474, 195561, 129738, 138268, 151612, 245726, 146338, 158597, 164824, 312177, 172489, 179812, 183272, 190038, 199171, 198642, 211856, 215253, 215847]

print(len(anzahl_array))
print(len(moves_array))
print(len(iterations_array))

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
