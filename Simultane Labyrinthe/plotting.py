import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

werte_l = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91]
iterations_array = [19912,
15677,
15224,
15090,
15020,
14929,
14975,
14791,
14792,
14733,
14851,
14761,
14792,
14808,
14725,
14779,
14805,
14680,
14656,]


plt.plot(werte_l, iterations_array, marker='', linestyle='-', color='b', label='tatsächliche Iterationen')
plt.plot()
plt.grid(True)
plt.xlabel('Begrenzung l' , fontsize=14)
plt.ylabel('Anzahl der Schritte' , fontsize=14)
plt.show()
