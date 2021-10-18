import logging 
import json
import pandas as pd
import math
import numpy as np

class Stat:
    def __init__(self): 
        logging.info('stats package initialized')

    def leastSquare(self, x, fn1, fn2):
        """
            loops over the overllaping rows
            and caluclates the least squared deviation
            between two functions

            this is used by the train and ideal functions
            to find the minimum squared deviation
        """
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
        """
            calculates the maximum deviation for two data frames
            accross the two provided columns
        """
        df = df1.merge(df2, on=0, how='left')
        df.dropna(inplace=True)
        return np.max(np.abs(df[df1_column] - df[df2_column]))
    
    def differentialDeviation(self, df1, df2): 
        """
            generates the difference in y values for two data frames
            and loads them into a new column called 'deviation'
        """
        df2 = df2[df2[0].isin(df1[0])]
        df = df1.merge(df2, on=0, how='left')
        df.columns = [0, 1, 2]
        df['deviation'] = abs(df[2]-df[1])
        return df

