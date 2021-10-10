from core.loaders.csvloader import csvloader;
from core.cleanser.csvcleanser import csvcleanser;
from core.stats import stats;
import json

path_test_data = './data/test.csv'
path_train_data = './data/train.csv'
path_ideal_data = './data/ideal.csv'

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
    print(best_fit)

    #calculate maximum deviation of regression
    fit = json.loads(best_fit)
    max_deviation = {}
    for key in fit:
        train_modified = trainData[[0,int(key)]].copy()
        ideal_modified = idealData[[0, fit[key]]].copy()
        max_deviation[key] = stat.maximumDeviationOfRegression(train_modified, ideal_modified, int(key), fit[key])
    print(max_deviation)

    #load test data and clean
    # test_data_importer = csvloader.CSVLoader(path_test_data, 'test.csv')
    # test_data_importer.read_csv()
    # test_data_importer.print_csv_info()

    # test_data_cleanser = csvcleanser.CSVCleanser(test_data_importer.csv_data, test_data_importer.label)
    # test_data_cleanser.print_cleansing_info()
    # test_data_cleanser.removeOutliers(1)

    # testData = test_data_cleanser.df;
    # ideaFunction=-1;
    # for key in fit:
    #     ideal_modified = idealData[[0, fit[key]]].copy()
    #     ideal_deviation = stat.maximumDeviationOfRegression(testData, ideal_modified, 1, fit[key])
    #     print(ideal_deviation)


if __name__ == '__main__':
    main()
