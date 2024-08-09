import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

# temperature
# temp_data = np.loadtxt("temperature.dat")
# ax1 = plt.axes()
# ax1.plot(temp_data[:,0], temp_data[:,1])

# dimensions
dime_data = np.loadtxt("dimensions.dat")
ax2 = plt.axes()
ax2.plot(dime_data[:,0], dime_data[:,2])
ax2.plot(dime_data[:,0], dime_data[:,3])
ax2.plot(dime_data[:,0], dime_data[:,4])


plt.show()