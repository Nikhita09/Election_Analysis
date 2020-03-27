#Data to be retrieve
import os
import csv
#Assign a variable for file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. total number of votes cast
#introduce variable
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #To read headers
    header = next(file_reader)
    #To print each row in csv file
    for row in file_reader:
        total_votes +=1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
for candidate,vote in candidate_votes.items():
    vote_percentage = format((float(vote)/float(total_votes))*100, '.2f')
    print(f"{candidate} has received {vote_percentage} % of the total votes\n")

for candidate,vote in candidate_votes.items():
    vote_percentage = format((float(vote)/float(total_votes))*100, '.2f')
    if (float(vote) > float(winning_count)) and (float(vote_percentage) > float(winning_percentage)):
        winning_count = vote
        winning_percentage = vote_percentage
        winning_candidate = candidate
    print(f"{candidate}: {vote_percentage}% ({vote:,})\n")
print(total_votes)   
print(candidate_options)
print(candidate_votes)

#2. complete list of candidated who received votes
#3. percentage of votes each candidate won
#4. total number of votes each candidate won
#5. winner of election