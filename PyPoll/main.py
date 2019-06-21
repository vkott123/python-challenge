#Python Homework
#Submitted By: Veena Kottoor

import os
import csv

# Joining path where the csv file is located
election_data = os.path.join('election_data.csv')

# Define/initialize variables
votes = []
candidates_unique = []
candidate_vote_count = []

# Open/Read the csv file
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:

        # Calculate total number of votes
        votes.append((row[2]))
        total_votes = len(votes)

        # Read through column 'C' of csv file
        # Find any unique candidates
        # Calculate each candidate's vote count

        candidate_list = (row[2])
        
        if candidate_list in candidates_unique:
            candidate_index = candidates_unique.index(candidate_list)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidates_unique.append(candidate_list)
            candidate_vote_count.append(1)

percentage = []
max_votes = candidate_vote_count[0]
max_index = 0

# Looping through the function for each unique candidate found (see above code)

for x in range(len(candidates_unique)):

    # Calculate the percentage of votes each candidate won

    vote_percentage = round(candidate_vote_count[x]/total_votes*100, 2)
    percentage.append(vote_percentage)

    # Determine the winner of the election based on popular vote
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

# Print election results to the terminal

print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for x in range(len(candidates_unique)):
    print(f"{candidates_unique[x]}: {percentage[x]}% ({candidate_vote_count[x]})")
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")


# Export a text file with the results

file = open("Election Results.txt","w")

file.write("Election Results")
file.write("\n-------------------------")
file.write(f"\nTotal Votes: {total_votes}")
file.write("\n-------------------------")
for x in range(len(candidates_unique)):
    file.write(f"\n{candidates_unique[x]}: {percentage[x]}% ({candidate_vote_count[x]})")
file.write("\n-------------------------")
file.write(f"\nWinner: {election_winner}")
file.write("\n-------------------------")

