#!/bin/python

import numpy as np
import pandas as pd

dates = pd.date_range('2014-01-01 00:00:00', periods=744, freq='1H')

for date in dates: 
	print date
