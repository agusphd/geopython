import matplotlib.pyplot as plt
import sqlite3
from numpy import array
import numpy as np

filename = './DATA/seismic.db'
conn = sqlite3.connect(filename)
c = conn.cursor()
c.execute('SELECT * FROM mytable WHERE value3 =10')
traces = [row[60:561] for row in c]
traces=(array(traces)).T


pol = 'Trough'

if pol == 'Peak':
    template = np.concatenate([[0] * 8, [1] * 1, [0] * 8])  # [1] if peak [-1] if through
elif pol == 'Trough':
    template = np.concatenate([[0] * 8, [-1] * 1, [0] * 8])  # [1] if peak [-1] if through
elif pol == 'None':
    template = np.concatenate([[0] * 8, [1] * 1, [0] * 8])  # [1] if peak [-1] if through

traces0=traces[:,0]
time = np.linspace(0,len(traces0)-1,len(traces0))*0.004



par4 = 0.1
df=[]
for i in range(60):
    trac=traces[:,i]
    trac = (trac - trac.mean()) / trac.std()
    try:
        corr_res = np.correlate(trac, template, mode='same')
        corr_res = corr_res / max(abs(corr_res))
        x = np.arange(len(corr_res))[abs(corr_res) > par4]
        yf = x[0]
    except:
        yf = 0
    plt.plot(1000 * i + traces[:,i], time, 'k')
    plt.plot(1000 * i + 0, yf*0.004, 'r.')
plt.ylim(2,0)
plt.show()
