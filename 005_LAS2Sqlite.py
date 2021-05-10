import numpy as np
import sqlite3

filename='./DATA/F03-2_logs.las'
data = np.loadtxt(filename,skiprows=35)
wellname ='F03'

conn = sqlite3.connect('well.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS %s (DEPTH real, RHOB real,DT real, GR real, AI real, AIr real, PHI real)'%wellname)
conn.commit()

cursor.executemany('INSERT INTO %s VALUES(?,?,?,?,?,?,?)' %wellname,map(tuple,data.tolist()))
conn.commit()




cursor.close()
conn.close()