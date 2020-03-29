import os
import csv
#Assign a variable for file to load and file to save along with path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Introduce all variables
total_votes = 0
candidate_options = []
county_options = []
candidate_votes = {}
county_votes = {}
winning_candidate = ""
largest_turnout = ""
winning_count = 0
turnout_count = 0
winning_percentage = 0
#Open and read file with data
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Skip counting header row
    header = next(file_reader)
    #To print each row in csv file
    for row in file_reader:
        total_votes +=1

        candidate_name = row[2]
        #To get list of candidates and number of votes each candidate received
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1

        county_name = row[1]
        #To get list of counties and number of votes each candidate received
        if county_name not in county_options:
            county_options.append(county_name)

            county_votes[county_name] = 0
        county_votes[county_name] +=1
#To print results in txt file
with open(file_to_save, "w") as txt_file:
    election_result = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_result,end="")
    txt_file.write(election_result)
    title = ("\nCounty Votes:\n")
    txt_file.write(title)
    #Calculate number and percentage of votes for each county 
    for county,turnout in county_votes.items():
        turnout_percent = format((float(turnout)/float(total_votes))*100,'.2f')
        county_results = (f"{county}: {turnout_percent}% ({turnout:,})\n")
        print(county_results)
        txt_file.write(county_results)
        #To find and print county with largest turnover
        if (float(turnout)> float(turnout_count)):
            turnout_count = turnout
            largest_turnout = county
    county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    txt_file.write(county_summary)
    print(county_summary)
    #To find and print winner of the election
    for candidate,vote in candidate_votes.items():
        vote_percentage = format((float(vote)/float(total_votes))*100, '.2f')
        if (float(vote) > float(winning_count)) and (float(vote_percentage) > float(winning_percentage)):
            winning_count = vote
            winning_percentage = float(vote_percentage)
            winning_candidate = candidate
        candidate_results = (f"{candidate}: {vote_percentage}% ({vote:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    summary = (
        f"-------------------------\nWinner : {winning_candidate}\nWinner Vote Count : {winning_count:,}\n"
        f"Winning Vote Percentage : {winning_percentage:.1f}%\n-------------------------\n")
    print(summary)
    txt_file.write(summary)