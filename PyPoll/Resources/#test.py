#test
import csv
with open("Resources\election_data.csv", "r") as f:
    #print(f)
    csvreader = csv.reader(f)
    print(csvreader)
    for row in csvreader:
        print(row)