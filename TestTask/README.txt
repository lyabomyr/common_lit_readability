For run ML should do next commands:
1. change directory to TestTask
2. enter command 'chmod u+x start.sh'
3. enter command './start'
Then will be installed all requirements libs, next will launched ml and create a directory 'result' with metrics, graph and submission.csv file
test.csv file by default is present in directory /Readability/csv_train_files/test.csv
To put ur own file u need to replace the test.csv file in /Readability/csv_train_files directory then enter the command ./start


How work my ML?
1. U print command  'chmod u+x start.sh; ./start.sh'  end my sh file will download lib and run Readability/main.py
2. launched  Readability/src/download.csv file (in this file script download csv train file and test from /Readability/csv_train_files/* )
3. launched  Readability/prepare_data.py file (in this file Ml  create X and Y for decision tree (for X ML takes  excerpt count words,
excerpt count character and excerpt sentiment(I used textblob lib for takes sentiments parametr)))
4. launched  Readability/training.py file for train and check our model from this file ML will create result
5. launched  Readability/result.py file for create submission.csv used already trained model.
6. launched Readability/main.py for run all this machine


How to start Server
1. Open terminal and run command 'chmod u+x start_server.sh; ./start_server.sh'
2. please wait until the server starts
3. open link "http://0.0.0.0:8000/docs#/default/create_file_files__post"
4. Next I hope you know how to use swager and can send a post request with a test.csv file
5. In response, u will receive zip file with folders then in last folder u wil be see three file graph, metrix and submission.csv



