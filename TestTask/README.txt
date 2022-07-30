For run ML should do next commands:
1. change directory to TestTask
2. enter command 'chmod u+x start.sh'
3. enter command './start'
then will be installed all requirements lib, next will make ml and create directory 'result' with metrix graph
Default test_file is present in directory /TestTask/Readability/csv_train_files/test.csv
For put ur file u can or change test.csv file in previous directory or just put file in test TestTask directory then enter command ./start
my start.sh file automatically move ur file in necessary directory for start.


How work my ML?
1. U print command  'chmod u+x start.sh; ./start.sh'  end my sh file will download lib and run Readability/main.py
2. launched  Readability/src/download.csv file (in this file script download csv train file and test from /Readability/csv_train_files/* )
3. launched  Readability/prepare_data.py file (in this file Ml  create X and Y for decision tree (for X ML takes  excerpt count words,
excerpt count character and excerpt sentiment(I used textblob lib for takes sentiments parametr)))
4. launched  Readability/training.py file for train and check our model from this file ML will create result
5. launched  Readability/result.py file for create submission.csv used already trained model.
6. launched Readability/main.py for run all this machine