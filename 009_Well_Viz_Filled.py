import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
file = './DATA/F02-1_logs.las'
data = np.loadtxt(file,skiprows=35)
data[data==-999.2500]=np.nan
mneumonics = ['DEPTH', 'RHOB', 'DT', 'GR', 'AI', 'AI_rel', 'PHIE']
data = pd.DataFrame(data, columns=mneumonics)
data = data[['DEPTH', 'RHOB', 'DT', 'GR']]
tb=  [0,464,539,612,635,687,702, 795, 814, 926, 949, 1026, 1053, 1095, 1133, 1270,1297, 1430,2000]
f = [1,2,3,1,3,4,3,1,3,1,3,1,3,1,3,4,3,1] #FACIES NO
depth = data.DEPTH.values
facies=[]
for i in range(len(depth)):
    for j in range(len(tb)-1):
        if depth[i] > tb[j] and depth[i] <=tb[j+1]:
            facies.append(f[j])
data['FACIES'] = facies

print(data)
data.to_csv('well1.csv', index=False)
data = data.values
mneumonics = [ 'RHOB', 'DT', 'GR', 'FACIES' ]
rows,cols = 1,4
fig,ax = plt.subplots(nrows=rows, ncols=cols, figsize=(12,10), sharey=True)
for i in range(cols):
    if i < cols-1:
        ax[i].plot(data[:,i+1], data[:,0], linewidth = '0.5', color='b')
        ax[i].set_ylim(max(data[:,0]), min(data[:,0]))
        ax[i].set_title('%s' % mneumonics[i])
        ax[i].minorticks_on()
        ax[i].grid(which='major', linestyle='-', linewidth='0.5', color='lime')
        ax[i].grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    elif i==cols-1:
        F = np.vstack((facies,facies)).T
        ax[i].imshow(F, aspect='auto', extent=[0,1,max(data[:, 0]), min(data[:, 0])])
        ax[i].set_title('%s' % mneumonics[i])
y2 = data[:,3]  #GR
y1 = y2*0+60 #60 API is Sand-Shale Boundary Line
ax[2].fill_betweenx(data[:,0],y1,y2,where=(y1>=y2), color = 'gold', linewidth=0)
ax[2].fill_betweenx(data[:,0],y1,y2,where=(y1<y2), color = 'lime', linewidth=0)
plt.show()