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
    print(f"{candidate}:")
