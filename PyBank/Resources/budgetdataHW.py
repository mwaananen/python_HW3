import os
import csv

#csvpath = os.path.join(C:\Users\mwaan\Desktop\DataBootCamp\Analysis Projects & HW\Homework\PythonHwWk1\Starter_Code\PyBank\Resources\budget_data.csv)
csvpath = r"C:\Users\mwaan\Desktop\DataBootCamp\Analysis Projects & HW\Homework\PythonHwWk1\Starter_Code\PyBank\Resources\budget_data.csv"
total_months = 1
change_sum = 0
month_change = []


with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
#Skip header
   csvheader = next(csvreader)
   row_one = next(csvreader)
#isolate first profit/loss number and set for use  
   net = int(row_one[1])
   val = int(row_one[1])
   change_sum = int(row_one[1])
#FOR LOOP (psuedocode equations and set initial parameters (lines 6,7,8))
   for row in csvreader:
      total_months += 1
      change_sum += int(row_one[1])
      month_change += [int(row[1]) - int(val)]
      net += int(row[1])
      val = int(row[1])
#identify final values OUTSIDE For Loop
average = sum(month_change)/len(month_change)
profit_gain = max(month_change)
profit_loss = min(month_change)
#Print values with text
print('Financial Analysis')
print('-----------------------------------------')
print('Total Months:', total_months)
print('Total:', change_sum)
print('Average of month-to-month change:', average)
print('Maximum month profit/loss:', profit_gain)
print('Minimum month profit/loss:', profit_loss)







   

 