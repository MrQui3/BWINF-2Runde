import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


anzahl_array = [1, 4, 5, 6, 7, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]
moves_array = [1374, 1243, 1157, 1185, 1176, 1106, 1132, 1137, 1068, 1124, 1128, 1132, 1069, 1069, 1070, 1076, 1068, 1070, 1068, 1055, 1065, 1065, 1055, 1055, 1057, 1057, 1057, 1055, 1057, 1041, 1041, 1053, 1053, 1053, 1043]
iterations_array = [1374, 2343, 2469, 2921, 3126, 5456, 6718, 8862, 12807, 11331, 12944, 24678, 26983, 28716, 28705, 32782, 33248, 37022, 36142, 38587, 43627, 45094, 41902, 43015, 44847, 46463, 47392, 47404, 49895, 45979, 46652, 56561, 55926, 57042, 52343]

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
