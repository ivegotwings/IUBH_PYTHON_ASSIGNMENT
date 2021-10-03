from core.loaders.csvloader import csvloader;

path_test_data = './data/test.csv'
path_train_data = './data/train.csv'
path_ideal_data = './data/idea.csv'

def main():
    test_data_importer = csvloader.CSVLoader(path_test_data, 'test.csv')
    test_data_importer.read_csv()
    test_data_importer.print_csv_info()

if __name__ == '__main__':
    main()
