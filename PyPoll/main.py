#import modules
import os
import csv

#create path for and open csv file

vote = os.path.join("PyPoll", "Resources", "election_data.csv")
with open(vote, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ",")
    #skip first row for header
    header = next(csvfile)

#loop through rows to count total votes

    total_votes = 0
    for row in csvreader:      
        total_votes += 1

#complete list of candidates who received votes
    #create candidate list dictionary
    candidates={}
    #get the candidate's name from the first row
    candidatename = row[2]

    #check if candidate name is dictionary
    if candidatename in candidates:
        candidates[candidatename] +=1
    else:   
        candidates[candidatename]=1

#The percentage of votes each candidate won
#create variable to store results
results =[]

#go through candidates and calculate percentage each candidate got
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))


#The winner of the election based on popular vote
#create variables to store max vote and winner
winner = ""
max_votes = 0

for candidate, votes, percentage in results:
    if votes>max_votes:
        max_votes = votes
        winner = candidate 

#print

print("Election Results")
print("-" *40)
print(f"Total Votes: {total_votes}")
print("-" *40)

for candidate, votes, percetange in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-" *40)
print(f"Winner: {winner}")
print("-" *40)