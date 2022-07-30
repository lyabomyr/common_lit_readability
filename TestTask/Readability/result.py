from training import *
from prepare_data import *

class CsvResult():

    def return_csv(self):
        model = TrainML().training_model_with_metrics()
        X_test = DataPrepare().prep_x('test')
        val_preds = model.predict(X_test[['count_words', 'count_chars', 'sentiment']])
        result = pd.DataFrame(X_test.id)
        result.loc[:, 'target'] = val_preds
        print(result)
        return result.to_csv('submission.csv', index=False)



