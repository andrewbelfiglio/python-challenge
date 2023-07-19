# Modules
import os
import csv

# Set path for the file
election_csv = os.path.join("Resources","election_data.csv")

# Declare initial vote total
vote_total = 0

# Create an empty dictionary to track votes for candidates
candidate_votes = {}

# Open the csv file and tally the votes
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Declare the header in the csv file
    csv_header = next(csvreader)

    # Search each row in the csv file
    for row in csvreader:
        
        # Add one to the vote total
        vote_total += 1

        # Identify the candidate in the third column
        candidate = row[2]

        # Check if the candidate is already in the dictionary
        if candidate in candidate_votes:
            
            # If yes, add one to their vote / value
            candidate_votes[candidate] += 1
            
        else:
            # If no, add them to the dictionary with vote / value = 1
            candidate_votes[candidate] = 1

# Create the list of candidates
candidate_list = [candidate for candidate in candidate_votes]

# Print the results table
print("Election Results")
print("--------------------")
print(f"Total Votes: {vote_total}")
print("--------------------")

# Calculate and print results for each candidate
for candidate in candidate_list:

    # Print the candidate's name, with the percentage of total votes rounded to 3 decimals, followed by the vote count
    print(f"{candidate}: {round((candidate_votes[candidate])/vote_total*100, 3)}% ({candidate_votes[candidate]} votes)")

# Print divider
print("--------------------")

# Find and print the winner, max votes from the candidate_votes dictionary
winner = max(candidate_votes, key = candidate_votes.get)
print(f"Winner: {winner}")

# Print divider
print("--------------------")

#---------------------------------------------------------------------------------
# SEND RESULTS TABLE TO TEXT FILE
#---------------------------------------------------------------------------------

# Re-direct the output to a txt file
# ~~~Re-direction code provided by luk32 (https://stackoverflow.com/users/1133179/luk32)
# ~~~luk32 code found in stackoverflow: https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file
import sys
f = open(os.path.join("Analysis", "output.txt"), 'w')
sys.stdout = f

# Results table code is copied / pasted from previous
# This will print the results again, but the output is being re-directed to a txt file
print("Election Results")
print("--------------------")
print(f"Total Votes: {vote_total}")
print("--------------------")

for candidate in candidate_list:
    print(f"{candidate}: {round((candidate_votes[candidate])/vote_total*100, 3)}% ({candidate_votes[candidate]} votes)")

print("--------------------")

winner = max(candidate_votes, key = candidate_votes.get)
print(f"Winner: {winner}")

print("--------------------")
# End of copied results table code

f.close()
# End of re-directing the output