

import os
import csv

output_file = "Election.txt"
txt_output_path = os.path.join(output_file)


total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

# open csv file
filepath = os.path.join("election_data.csv")
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # tally votes
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# calculate vote percentage and identify winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

dashbreak = "-------------------------"

# print out results
print("Election Results")
print(dashbreak)
print(f"Total Votes: {total_votes}")
print(dashbreak)
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

# save summary to txt

with open(txt_output_path, mode='w', newline='') as POLsummary_txt:
    writer = csv.writer(POLsummary_txt)
    POLsummary_txt.write(dashbreak + "\n")
    POLsummary_txt.write(f"Total Votes: {total_votes}" + "\n")
    POLsummary_txt.write(dashbreak + "\n")
    for person, vote_count in candidate_votes.items():
        POLsummary_txt.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
    POLsummary_txt.write(dashbreak + "\n")
    POLsummary_txt.write(f"Winner: {winner}" + "\n")
    POLsummary_txt.write(dashbreak + "\n")
