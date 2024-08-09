import matplotlib.pyplot as plt
import numpy as np

reflect_count = 0
implant_count = 0
depths = []

for i in range(1,5):
    file = open("../data-deckard-4k/data-1k-chunk-"+str(i)+".txt", "r")
    lines = file.readlines()

    for line in lines:
        data = line.strip().split(" ")
        posZ = float(data[3])
        surfaceZ = float(data[4])
        depth = surfaceZ - posZ

        if depth <= 0:
            reflect_count += 1
        else: 
            implant_count += 1
            depths.append(depth)
        
    file.close()

outlier = depths.index(max(depths))
depths.pop(outlier)

depths = np.array(depths)
# Plotting a basic histogram
bins = [i/6.0 for i in range(0, 390, 10)]
plt.hist(depths, bins=bins, color='skyblue', edgecolor='black')
plt.xlim(0)
 
# Adding labels and title
plt.xlabel('Depth (Angstroms)')
plt.ylabel('Occurences')
plt.title('Implantation Depth')
 
# Display the plot
plt.show()