#Data to be retrieve
import os
import csv
#Assign a variable for file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    print(next(file_reader))
#1. total number of votes cast
#2. complete list of candidated who received votes
#3. percentage of votes each candidate won
#4. total number of votes each candidate won
#5. winner of election