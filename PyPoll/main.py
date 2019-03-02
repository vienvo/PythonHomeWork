#PyPoll Homework

#Import dependencies
import os
import csv

# Setup path
electionCSV = os.path.join("..","PyPoll","election_data.csv")

# Create list to hold values
votes = []
results = {}

# Open the budget file and create list votes which include all vote by name
with open(electionCSV,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    # Loop file to get total, months, and list of profits & months
    for row in csvreader:
        votes.append(row[2])

# Count total votes
totalvotes = len(votes)

# Create unique list of candidates
candidates = (set(votes))
candidates = list(candidates)
candidates.sort()
number_of_candidates = len(candidates)

# Create results dictionary
i = 0
while i <= (number_of_candidates - 1):
    results[candidates[i]] = votes.count(candidates[i])
    i += 1

#Election results to terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalvotes}')
print('-------------------------')
for c, v in results.items():
    print(f'{c}: {round((v/totalvotes)*100,2)}% ({v})')

#Determine Winner
max_vote = max(results.values())
for c, v in results.items():
    if v == max_vote:
        print('-------------------------')
        print(f'Winner: {c}')
        print('-------------------------')

# Return results to output text file
with open('pyPoll_output.csv','w',newline='') as csvOutput:
    csvwriter = csv.writer(csvOutput,delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Votes: ', (totalvotes)])
    csvwriter.writerow(['----------------------------'])
    for c, v in results.items():
        csvwriter.writerow([f'{c}: {round((v/totalvotes)*100,2)}% ({v})'])
    for c, v in results.items():
        if v == max_vote:
            csvwriter.writerow(['-------------------------'])
            csvwriter.writerow([f'Winner: {c}'])
            csvwriter.writerow(['-------------------------'])   
