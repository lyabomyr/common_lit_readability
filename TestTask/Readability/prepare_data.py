from src.download_csv import *
from textblob import TextBlob

class DataPrepare():

    def get_data(self, file_name):
        return Data().get_exel_file(file_name)

    def prep_x(self,file_name):
        train_data = self.get_data(file_name)
        x_data = pd.DataFrame(train_data['id'])
        x_data['count_words'] = train_data.excerpt.str.split().apply(lambda x_data: len(x_data))
        x_data['count_chars'] = train_data.excerpt.str.len()
        x_data['sentiment'] = train_data.excerpt.apply(lambda x_data: TextBlob(x_data).sentiment.polarity)
        return x_data

    def prep_y(self, file_name):
        return self.get_data(file_name).target



