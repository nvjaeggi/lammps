import os

import matplotlib.pyplot as plt
import numpy as np

# Get the list of all files and directories
path = "/mnt/c/Users/annbe/OneDrive/Desktop/vico/tungsten/graphs/100-implanted"
dir_list = os.listdir(path)
depths = []

for dir in dir_list:
    if dir[12] == '.': num = int(dir[11:12])
    else: num = int(dir[11:13])

    file = open("data/He_run"+str(num)+".txt", "r")
    for line in file:
        pass
    last_line = line

    v = last_line.strip().split(" ")
    depth = float(v[2]) - float(v[0])
    depths.append(depth)


depths = np.array(depths)
# Plotting a basic histogram
plt.hist(depths, bins=12, color='skyblue', edgecolor='black')
 
# Adding labels and title
plt.xlabel('Depth (Angstroms)')
plt.ylabel('Frequency')
plt.title('Implantation Depth')
 
# Display the plot
plt.show()