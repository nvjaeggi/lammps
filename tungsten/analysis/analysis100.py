import matplotlib.pyplot as plt
import numpy as np

for i in range(1,101):
    file = open("data/He_run"+str(i)+".txt", "r")
    lines = file.readlines()
    velZ = []
    posZ = []
    surfaceZ = []

    for line in lines:
        if line[0] == "#": continue
        data = line.strip().split(" ")
        posZ.append(float(data[0]))
        velZ.append(float(data[1]))
        surfaceZ.append(float(data[2]))

    file.close()

    dt = 0.0002
    frame_rate = 50
    x = np.arange(len(posZ)) * dt * frame_rate



    # position of He atom and surface
    y1 = np.array(posZ)
    y2 = np.array(surfaceZ)
    plt.plot(x, y1, label='Helium atom')
    plt.plot(x, y2, label='Tungsten surface')
    plt.ylabel("position (Angstroms/ps)")
    plt.title('position in the z-direction')
    plt.legend()

    # velocity of He atom
    # y3 = np.array(velZ)
    # plt.plot(x, y3)
    # plt.ylabel("velocity (Angstroms/ps)")
    # plt.title('velocity in the z-direction')

    plt.xlabel("time (picosecond)")
    plt.savefig('graphs/100/He-position'+str(i)+'.png')
    plt.clf()
    # plt.show() 