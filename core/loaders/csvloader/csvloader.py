from numpy import genfromtxt
import logging 
import traceback
import json

class CSVLoader:
    """
        Modules loads data from csv file in a pandas dataframe
        the csv_info method can be used to generate information about the data
    """
    def __init__(self, path, label):
        self.csv_file_path = path
        self.label = label
    
    def read_csv(self):
        data = genfromtxt(self.csv_file_path, delimiter=',', skip_header=True, converters={0: lambda num: float(num)})
        self.csv_data = data
        self.csv_data_info = self.csv_info(data)

    def csv_info(self, data):
        info = {}
        try:
            info['size'] = data.size
            info['shape'] = data.shape
            info['dimensions'] = data.ndim
            info['type'] = str(data.dtype)
            info_json = json.dumps(info)
        except Exception:
            logging.exception('unable to read data from CSV file: %s', data)
            traceback.print_exc()
            raise
        return info_json

    def print_csv_info(self):
        print('file information for {}: {}'.format(self.label, self.csv_data_info))
