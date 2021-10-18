import logging 
import traceback
import json
import pandas as pd
from numpy import mean
from numpy import std

class CSVCleanser:
    """
        This module provides functionality to clean the csv data loaded using the loader module
    """
    def __init__(self, ndarray, label):
        self.data = ndarray
        self.label = label
        self.df = pd.DataFrame(self.data)

    
    def __clean_info(self):
        """
            provides information about the data after
                removing duplicates
                remonin na
                sroting by first column
        """
        info = {}
        try:
            df = self.df
            df.sort_values(0, inplace=True)
            len_before_removing_duplicates = len(df)
            df.drop_duplicates(inplace=True)
            len_after_removing_duplicates = len(df)
            info['columns_with_na'] = df.columns[df.isna().any()].tolist()
            info['num_columns'] = len(df.columns)
            info['sorted_by_index'] = 0
            info['removed_duplicated'] = len_before_removing_duplicates - len_after_removing_duplicates
            info_json = json.dumps(info)
        except Exception:
            logging.exception('unable to read cleansing info data of %s from data frame: %s', self.label)
            traceback.print_exc()
            raise
        return info_json

    def __outlier_info(self, col):
        """
            private function
            finds outliers using mean and deviation
        """
        df = pd.DataFrame(self.data)
        data = df[col].to_numpy()

        # calculate summary statistics
        # value which are more than 2 standard deviations difference are considered outliers.
        data_mean, data_std = mean(data), std(data)
        # identify outliers
        cut_off = data_std * 2
        lower, upper = data_mean - cut_off, data_mean + cut_off

        outliers = [x for x in data if x < lower or x > upper]
        return outliers

    def __filter_rows_by_values(self, df, col, values):
        return df[~df[col].isin(values)]

    def removeOutliers(self, col): 
        """
            removes outliers using the __filter_rows_by_values private function utility
        """
        self.df.sort_values(0, inplace=True)
        self.df.drop_duplicates(inplace=True)
        outliers = self.__outlier_info(col)
        self.df = self.__filter_rows_by_values(self.df, col, outliers)

    def print_cleansing_info(self):
        print('cleaning file information for {}: {}'.format(self.label, self.__clean_info()))
