import pandas as pd
import os


class Data():
    def get_exel_file(self, file):
        global data_frame
        repl = ['/src', '/Readability/csv_train_files/']
        patch_to_file = (os.getcwd() + repl[1])

        if file == 'train':
            data_frame = pd.read_csv(f'{patch_to_file}train.csv')
        if file == 'test':

            data_frame = pd.read_csv(f'{patch_to_file}test.csv')
        return data_frame

