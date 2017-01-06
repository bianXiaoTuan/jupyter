#!/bin/python

import random

if __name__ == '__main__':
    NUM = 744
    temperatures = []
    dew_points = []
    pressures = []

    for i in range(744):
        temperatures.append(round(70 + random.random() * 30, 1))
        dew_points.append(round(50 + random.random() * 30, 1))
        pressures.append(round(random.random() * 2, 1))
    
    temperatures.sort()
    dew_points.sort()
    pressures.sort()

    for i in range(NUM):
        print '%0.1f,%0.1f,%0.1f' % (temperatures[i],dew_points[i],pressures[i])
