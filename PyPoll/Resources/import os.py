import os
import csv

csvpath = r"C:\Users\mwaan\Desktop\DataBootCamp\Analysis Projects & HW\Homework\PythonHwWk1\Starter_Code\PyPoll\Resources\election_data.csv"



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)