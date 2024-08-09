import matplotlib.pyplot as plt
import numpy as np

file = open("temp_data.txt", "r")
lines = file.readlines()
temp = []
time = []

for line in lines:
    data = line.strip().split()
    temp.append(float(data[4]))
    time.append(float(data[1]))
    
file.close()

x = np.array(time)
y = np.array(temp)

plt.plot(x, y)
plt.axvline(x=500, color='r', linestyle='--', linewidth=2)
# for i in range(0, 50, 5):
#     plt.axvline(x=i, color='r', linestyle='--', linewidth=2)

plt.xlabel("time (picosecond)")
plt.ylabel("number of implanted Helium atoms")
plt.title('100 atoms')

plt.show()