import matplotlib.pyplot as plt
import numpy as np

file = open("data-cube-bombard/thermo_try5.out", "r")
lines = file.readlines()
pressure = []
time = []

started = False

for line in lines:
    data = line.strip().split()
    if started:
        if not data[0].isnumeric(): break
        pressure.append(float(data[3]))
        time.append(float(data[1]))
    if data[0] == "Step": started = True
    
file.close()

x = np.array(time)
y = np.array(pressure)

plt.plot(x, y)
# for i in range(0, 50, 5):
#     plt.axvline(x=i, color='r', linestyle='--', linewidth=2)

plt.ylabel("temperature (Kelvin)")
plt.xlabel("time (picoseconds)")
plt.title('Small Cube Bombardment Temperature')

plt.show()