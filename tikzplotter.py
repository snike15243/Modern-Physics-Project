import matplotlib.pyplot as plt
import tikzplotlib

from Responsivity_newdata import responsivities, responsivities2, amplitudes_values

plt.style.use('default')
fig, ax = plt.subplots()
ax.plot(amplitudes_values, responsivities)
ax.plot(amplitudes_values, responsivities2)
#plt.show()
tikzplotlib.clean_figure()

tikzplotlib.save("responsivities.tex")