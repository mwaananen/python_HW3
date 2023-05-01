import os
import csv
#File import has not been working/terminal problems
csvpath = "Resources\election_data.csv"
#defined list - complete when new definition as needed
votes = 0
namelist = []
total_for_name = {}
win_total = 0
winner = ""

#Open file 
#fix path
#with open(csvpath,"r") as electiondata:
with open("Resources\election_data.csv", "r") as f:
    csvreader = csv.reader(f)
#skip header
    header = next(csvreader)
    #For Loop with 2 directives
    for row in csvreader:
        votes += 1
        name = row[2]
        #IF statement (not/in recognized by python)
        if name not in namelist:
            namelist.append(name) #needs further explanation
            total_for_name[name] = 0 #start with 0
        total_for_name[name] += 1 #same as Votes above(will need later)
    print("Election results")
    print("------------------")
    print(f"Total votes: {votes}") #all votes, not candidate specific, despite total_for_name & namelist
    print("------------------")
    #For Loop Key and Value 
    for k,v in total_for_name.items(): #totals for candidates from above
        vote_percent = v/votes * 100 #Value(v) used to determine percentage
        print(f"{k}: {vote_percent}%")
        print(vote_percent)
        if v > win_total: #if the value in the total_for_name is greater than the win total...
            win_total = v #then that value is the win total, and the key/candidate is the winner
            winner = k

    print(votes)
    print(namelist)
    print(total_for_name)
    print(winner)


