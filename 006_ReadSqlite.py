import sqlite3
import numpy as np
import pandas as pd

conn = sqlite3.connect('well.db')
c = conn.cursor()
c.execute('SELECT * FROM F02 WHERE DEPTH > 1000')

data = [row for row in c]
data = np.array(data)
data[data==-999.2500]=np.nan

data = pd.DataFrame(data,columns=['DEPTH', 'RHOB', 'DT', 'GR', 'AI', 'AIr', 'PHI'])
print(data)
