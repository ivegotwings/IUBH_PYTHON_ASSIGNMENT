from core.loaders.csvloader import csvloader;
from core.cleanser.csvcleanser import csvcleanser;
from core.stats import stats;
import json
import math
from functools import reduce
import pandas as pd


path_test_data = './data/test.csv'
path_train_data = './data/train.csv'
path_ideal_data = './data/ideal.csv'

def testDataAnalysis(deviations, max_deviation, key):
    """
        this function uses the criterion for selection of an ideal function
        and drops all the deviations are more the sqrt(2) of the caluclated 
        deviation of regression found by using the train functions
    """
    df = deviations
    df = df.drop(df[df['deviation'] >  max_deviation * math.sqrt(2)].index)
    df.columns = ['x', 'test-y', key, 'delta-y_'+key]
    return df

def main():
    stat = stats.Stat()


    # load train data set
    train_data_importer = csvloader.CSVLoader(path_train_data, 'train.csv')
    train_data_importer.read_csv()
    train_data_importer.print_csv_info()

    #clean train data set
    train_data_cleanser = csvcleanser.CSVCleanser(train_data_importer.csv_data, train_data_importer.label)
    train_data_cleanser.print_cleansing_info()
    trainData = train_data_cleanser.df

    #load ideal data set
    ideal_data_importer = csvloader.CSVLoader(path_ideal_data, 'ideal.csv')
    ideal_data_importer.read_csv()
    ideal_data_importer.print_csv_info()

    #clean ideal data set
    ideal_data_cleanser = csvcleanser.CSVCleanser(ideal_data_importer.csv_data, ideal_data_importer.label)
    ideal_data_cleanser.print_cleansing_info()
    
    #generate best fit
    idealData = ideal_data_cleanser.df
    best_fit = stat.leastSquare(trainData[0].to_numpy(), trainData, idealData)

    #calculate maximum deviation of regression
    fit = json.loads(best_fit)
    max_deviation = {}
    for key in fit:
        train_modified = trainData[[0,int(key)]].copy()
        ideal_modified = idealData[[0, fit[key]]].copy()
        max_deviation[key] = stat.maximumDeviationOfRegression(train_modified, ideal_modified, int(key), fit[key])

    # load test data and clean
    test_data_importer = csvloader.CSVLoader(path_test_data, 'test.csv')
    test_data_importer.read_csv()
    test_data_importer.print_csv_info()

    test_data_cleanser = csvcleanser.CSVCleanser(test_data_importer.csv_data, test_data_importer.label)
    test_data_cleanser.print_cleansing_info()
    test_data_cleanser.removeOutliers(1)

    testData = test_data_cleanser.df

    """ 
        Calculate the differential for each point in the test data
        and store the result in a csv per ideal function
        output director has 4 files each correspoding to 1 ideal function
    """
    data_frames = []
    for i in range(len(testData.columns)):
        for key in fit:
            ideal_modified = idealData[[0, fit[key]]].copy()
            deviations = stat.differentialDeviation(testData, ideal_modified); 
            matchDf = testDataAnalysis(deviations, max_deviation[key], 'ideal-'+str(fit[key])+'_y')
            matchDf.to_csv('data/csv/output/' + 'ideal-'+str(fit[key]) + '.csv')
            data_frames.append(matchDf)
    
    """
        The merged data frames combines the y devations calulations
        across all the ideal functions
        output.cs contains the total information for
        all test data points accross the 4 selected ideal functions
    """
    df_merged = pd.concat(data_frames)
    df_merged_temp = df_merged.drop(['x','test-y'],axis=1)
    count = df_merged_temp.loc[:].count(axis=1)
    df_merged['count'] = count
    df_merged.to_csv('data/csv/output/output.csv')


if __name__ == '__main__':
    main()
