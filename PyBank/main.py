#import modules
import os
import csv


# Define the path to the csv file
budget_data_path = os.path.join( "PyBank", "Resources", "budget_data.csv")

# create variables to store financial analysis
total_months = 0
net_total = 0
prev_profit_loss = 0
changes = []
dates = []

# read the csv file
with open(budget_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    header = next(csvreader)

 # Loop through each row in the CSV file
    for row in csvreader:
     # Extract date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the net total
        net_total += profit_loss

        # changes in "Profit/Losses" over the entire period
        if total_months != 0:
            change = profit_loss - prev_profit_loss
            changes.append(change)
            dates.append(date)

        # update previous profit/loss
        prev_profit_loss = profit_loss

        # Increment the total number of months
        total_months += 1

# average of those changes
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the financial analysis results
#for decimal place print out https://realpython.com/python-modulo-string-formatting/#:~:text=To%20insert%20a%20percent%20character,that%20the%20conversion%20type%20is%20%25%20.
print("Financial Analysis")
print("-"*40)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#create output path for .txt file
output_path = os.path.join("PyBank", "analysis", "Financial_Analysis.txt")
#export to txt file
with open(output_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-"*40 + "\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
