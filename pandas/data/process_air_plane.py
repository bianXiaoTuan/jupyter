#!/bin/python

import random
import numpy as np
import pandas as pd

citys = ['!!hangzhou!', '!!shanghai!', '!beijing', '!!wuhan', '!!shenzheng!!']
dates = pd.date_range('2014-01-01 00:00:00', periods=8759, freq='1H')

print 'date,city'
for date in dates:
	print '%s,%s' % (date, citys[int(random.random() * 5)])





