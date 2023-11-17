import csv
import os

# define the file path
vote_path = os.path.join("PyPoll", "Resources", "election_data.csv")

# create variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

#open the file
with open(vote_path, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ",")
    
       # skip the header row
    header = next(csvreader)

    # loop through each row
    for row in csvreader:
        # count total votes
        total_votes += 1

        # count votes for each candidate registering new candidate name as it goes along
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Print the election results
print("Election Results")
print("-"*40)
print(f"Total Votes: {total_votes}")
print("-"*40)

# calculate percentage of vote per candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    #print results with percentage
    #for percentage/decimal place printout
    #  https://realpython.com/python-modulo-string-formatting/#:~:text=To%20insert%20a%20percent%20character,that%20the%20conversion%20type%20is%20%25%20.
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # check for maximum votes
    if votes > max_votes:
        winner = candidate
        max_votes = votes

# print the winner (maximum votes)
print("-"*40)
print(f"Winner: {winner}")
print("-"*40)

#create output path for .txt file
output_path = os.path.join("PyPoll", "analysis", "Poll.txt")
#export to txt file
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("-"*40+"\n")
    file.write(f"Total Votes: {total_votes}\n")
    for candidate, result in candidates.items():
        file.write(f"{candidate}: {['percentage']}% ({result['votes']})\n")
    file.write("-"*40+"\n")
    file.write(f"Winner: {winner}\n")
    file.write("-"*40+"\n")
   
    
    
    
    
  