#Importing 
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first 
    csv_header = next(csvreader)
    data = list(csvreader)
    votes_count = len(data)

  # Create new list from CSV column 
    candidate_list = list()
    votePer_candidate = list()
    for i in range (0,votes_count):
        candidate = data[i][2]
        votePer_candidate.append(candidate)
        if candidate not in candidate_list: 
            candidate_list.append(candidate)
    candidate_count = len(candidate_list)
   

  # The total number of votes each candidate won 
    votes = list()
    percentage = list()
    for i in range (0,candidate_count):
        name = candidate_list[i]
        votes.append(votePer_candidate.count(name))
        vote_percent = votes[i]/votes_count
        percentage.append(vote_percent)
   
  # The winner of the election 
    winner = votes.index(max(votes))    


  # Print the results to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {votes_count:}")
    print("----------------------------")
    for i in range (0,candidate_count): 
        print(f"{candidate_list[i]}: {percentage[i]:.3%} ({votes[i]:})")
    print("----------------------------")
    print(f"Winner: {candidate_list[winner]}")
    print("----------------------------")

  # Exporting the result
    output_file = open("Election_Result.txt", "w")
    output_file.write("Election Result\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {votes_count:}\n")
    output_file.write("----------------------------\n")
    for i in range (0,candidate_count): 
        output_file.write(f"{candidate_list[i]}: {percentage[i]:.3%} ({votes[i]:})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {candidate_list[winner]}\n")
    output_file.write("----------------------------\n")




    