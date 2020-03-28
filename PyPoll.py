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

with open(file_to_save, "w") as txt_file:
    election_result = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_result,end="")
    txt_file.write(election_result)

    for candidate,vote in candidate_votes.items():
        vote_percentage = format((float(vote)/float(total_votes))*100, '.2f')
        print(f"{candidate} has received {vote_percentage} % of the total votes\n")

    for candidate,vote in candidate_votes.items():
        vote_percentage = format((float(vote)/float(total_votes))*100, '.2f')
        if (float(vote) > float(winning_count)) and (float(vote_percentage) > float(winning_percentage)):
            winning_count = vote
            winning_percentage = float(vote_percentage)
            winning_candidate = candidate
        candidate_results = (f"{candidate}: {vote_percentage}% ({vote:,})\n")
        #print(candidate_results)
        txt_file.write(candidate_results)
    print(total_votes)  
    
    print(candidate_options)
    
    print(candidate_votes)
    summary = (
        f"-------------------------\nWinner : {winning_candidate}\nWinner Vote Count : {winning_count:,}\n"
        f"Winning Vote Percentage : {winning_percentage:.1f}%\n-------------------------\n")
    #print(summary)
    txt_file.write(summary)