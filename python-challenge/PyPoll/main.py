# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = [] # list that holds the candidates
candidate_votes = {} #dictionary the will hold vote each candidate recieves 

# Winning Candidate and Winning Count Tracker
winningCount = 0
winner =""
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row


        # If the candidate is not already in the candidate list, add them
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        
        


        # Add a vote to the candidate's count
        else :  
            candidate_votes[row[2]] +=1



#print(candidate_votes)

vote_output = ""
for candidate in candidate_votes:
    vote = candidate_votes.get(candidate)
    votePct = 100*(float(vote)/float(total_votes))

    vote_output += f"\n{candidate} {votePct:.3f}% ({vote:,}) \n"

    #finding the winner
    if vote > winningCount:
        winningCount = vote
        winner = candidate
winnerOutput = f"\nWinner: {winner}\n\n--------------------- "  
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    output = (
        f"\n\nElection Results\n"
        f"---------------------\n"
        f"\nTotal Votes: {total_votes:,} \n"
        f"\n---------------------\n"
        f"{vote_output}"
        f"\n---------------------\n"
        f"{winnerOutput}"
    )
    print(output)
    # Write the total vote count to the text file
    txt_file.write(output)
