import lasio
import matplotlib.pyplot as plt

filename = './DATA/F02-1_logs.las'
data = lasio.read(filename)
data = data.df()

DEPTH = list(data.index.values)
DT = (list(data['DT'.strip()]))

plt.plot(DT,DEPTH)
plt.grid()
plt.ylim(1500,250)
plt.show()