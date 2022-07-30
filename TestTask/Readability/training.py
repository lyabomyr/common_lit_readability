from prepare_data import *
from sklearn.model_selection import train_test_split
from sklearn.tree import *
from sklearn.metrics import *
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt




class TrainML():

    def training_model_with_metrics(self):
        global train_preds
        X = DataPrepare().prep_x('train').iloc[:,1:4]
        y = DataPrepare().prep_y('train')

        train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
        confusion_matrix = pd.DataFrame(columns=['train_error', 'val_error', 'num_leaf'])

        for max_leaf_nodes in range(2, 100):
            model = DecisionTreeRegressor(random_state=0, max_leaf_nodes=max_leaf_nodes)
            model.fit(train_X, train_y)
            train_preds = model.predict(train_X)
            train_e = np.sqrt(mean_absolute_error(train_y, train_preds))
            # print(f'result for mean_absolute_error for train error MSE = {train_e}')
            val_preds = model.predict(val_X)
            val_e = mean_absolute_error(val_y, val_preds)
            confusion_matrix.loc[max_leaf_nodes - 2] = [train_e, val_e,
                                                        model.get_n_leaves()]  # train_e = MSE for train_error,\
            # val_e = MSE for val_error #get_n_leaves() = number of leaves of the decision tree



        fig, simple_chart = plt.subplots()
        simple_chart.plot(confusion_matrix['train_error'], confusion_matrix['num_leaf'])
        simple_chart.plot(confusion_matrix['val_error'], confusion_matrix['num_leaf'])
        plt.savefig('confusion_matrix.png', bbox_inches = 'tight', facecolor='red')

        model = DecisionTreeRegressor(random_state=0, max_leaf_nodes=24)
        model.fit(train_X, train_y)
        #y_pred = model.predict(X)

        #print(f'first 5 confusion matrix param for example{confusion_matrix.head()}')
        #print(f'MSE for train error {confusion_matrix.train_error.mean()}')
        #print(f'MSE for val error {confusion_matrix.val_error.mean()}')
        #print(f' for simple train r2 score {r2_score(y, y_pred)}')

        model = DecisionTreeRegressor(random_state=0, max_leaf_nodes=24)
        model.fit(train_X, train_y)

        print(f'MAE for train prediction {mean_absolute_error(train_y,train_preds)}')
        print(f'for MSE for val prediction {np.sqrt(metrics.mean_squared_error(train_y,train_preds))}')

        return model







