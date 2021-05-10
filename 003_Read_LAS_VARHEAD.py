import numpy as np
import matplotlib.pyplot as plt

filename='./DATA/F03-2_logs.las'
mark = '~A'
with open(filename) as myFile:
    for z, line in enumerate(myFile, 1):
        if mark in line:
            data = np.loadtxt(filename, skiprows=z)
            data[data == -999.2500] = np.nan
            DEPTH = data[:, 0]
            DENS = data[:, 1]
            SONIC = data[:, 2]
            GR = data[:, 3]

            plt.subplot(1, 3, 1)  # row-col-colth
            plt.plot(DENS, DEPTH, 'b')
            plt.ylim(max(DEPTH), min(DEPTH))
            plt.xlabel('Density [kg/m3]')
            plt.ylabel('Measured Depth [m]')

            plt.subplot(1, 3, 2)  # row-col-colth
            plt.plot(SONIC, DEPTH, 'r')
            plt.ylim(max(DEPTH), min(DEPTH))
            plt.xlabel('Sonic [us/m]')
            plt.ylabel('Measured Depth [m]')

            plt.subplot(1, 3, 3)  # row-col-colth
            plt.plot(GR, DEPTH, 'g')
            plt.ylim(max(DEPTH), min(DEPTH))
            plt.xlabel('GR [API]')
            plt.ylabel('Measured Depth [m]')
            plt.show()
