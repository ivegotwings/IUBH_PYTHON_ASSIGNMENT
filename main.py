from core.loaders.csvloader import csvloader;
from core.cleanser.csvcleanser import csvcleanser;

path_test_data = './data/test.csv'
path_train_data = './data/train.csv'
path_ideal_data = './data/ideal.csv'

def main():
    test_data_importer = csvloader.CSVLoader(path_test_data, 'test.csv')
    test_data_importer.read_csv()
    test_data_importer.print_csv_info()

    test_data_cleanser = csvcleanser.CSVCleanser(test_data_importer.csv_data, test_data_importer.label)
    test_data_cleanser.print_cleansing_info()

    test_data_cleanser.clean(1)
if __name__ == '__main__':
    main()
