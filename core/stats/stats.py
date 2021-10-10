import logging 
import json
import pandas as pd
import math
import numpy as np

class Stat:
    def __init__(self): 
        logging.info('stats package initialized')

    def leastSquare(self, x, fn1, fn2):
        #filter values of x in 2 that are not in 1
        fn2 = fn2[fn2[0].isin(x)]
        info = {}
        for i in range(len(fn1.columns)): 
            if(i == 0): continue
            minSum = math.inf
            for j in range(len(fn2.columns)):
                sum = 0
                if j == 0: continue
                y1 = fn1[i].to_numpy()
                y2 = fn2[j].to_numpy()
                for k in range(len(y1)):
                    sum += (y1[k]-y2[k]) * (y1[k]-y2[k])
                if (sum < minSum):
                    minSum = sum
                    info[i] = j
        
        info_json = json.dumps(info)
        return info_json

    def maximumDeviationOfRegression(self, df1, df2, df1_column, df2_column):
        df = df1.merge(df2, on=0, how='left')
        df.dropna(inplace=True)
        return np.max(np.abs(df[df1_column] - df[df2_column]))
