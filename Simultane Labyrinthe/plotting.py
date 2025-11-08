import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

werte_l = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91]
theoretichses_iterations = [30600,
183600,
336600,
489600,
642600,
795600,
948600,
1101600,
1254600,
1407600,
1560600,
1713600,
1866600,
2019600,
2172600,
2325600,
2478600,
2631600,
2784600]
iterations_array = [19912,
39767,
56713,
70876,
83444,
91470,
108082,
109927,
124064,
129124,
149405,
155943,
174149,
179896,
189500,
194468,
190191,
199651,
198909]
plt.rcParams['text.usetex'] = True


plt.plot(werte_l, iterations_array, marker='', linestyle='-', color='b', label='tatsächliche Iterationen')
plt.plot(werte_l, theoretichses_iterations, marker='', linestyle='-', color='g', label='maximale Iterationen')
plt.plot()
plt.grid(True)
plt.legend(fontsize=12)
plt.xlabel(r'Begrenzung $l$', fontsize=15)
plt.ylabel('Anzahl der Schritte', fontsize=15)
plt.show()











v = ("Wir waren einfach 13 Jahre lang in der selben Klasse und seit Anfang an befreundet. Früher noch Hortzeit mit Benji, dann Mittagsbetreuung im Gymnasium und jetzt mit Krypto und all den anderen."
    "Früher noch im Hort mit Benji und jetzt mit Krypto und all den anderen. Ich hoffe, dass wir auch noch in 13 Jahren befreundet sind. ")

e = ("Unsere Robotik-Freitagsnachmittage war zu krass. dann immer Unterricht geschwänzt bei IT-Notfall und Technik Team. Hast entweder im Unterricht geschlafen oder warst nur am IPad. "
     "Und dann die Nachricht eine Abend vor dem Vokabeltest, der über 20 Seiten ging. Und trotzdem warst du immer besser als ich im Vokabeltest."
     " Wir haben keine einziges Projekt vor einem tag davor angefangen und noch nie im Oberstufenraum gearbeitet. ")