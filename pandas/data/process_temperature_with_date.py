#!/bin/python

import random
import numpy as np
import pandas as pd

dates = pd.date_range(start='2008-01-01 00:00:00', end='2012-01-01 00:00:00', freq='1H')

print 'Date,Temperature,DewPoint,Pressure'
for date in dates: 
	print '%s,%0.1f,%0.1f,%0.1f' % (date, random.random() * 10 + 40, random.random() * 10 + 30, random.random() * 3)
