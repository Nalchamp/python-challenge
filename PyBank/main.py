#import modules
import os
import csv

#create path for csv file
budget_path = os.path.join( "PyBank", "Resources", "budget_data.csv")

#open the file
with open(budget_path, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    #define the data as a list
    data=list(csvreader)

#The total number of months included in the dataset. count number of rows
Num_Mths = len(data)
print (Num_Mths)
#The net total amount of "Profit/Losses" over the entire period
#definte the function
def print_total(budget_data):
    Date = str(budget_data[0])
    Profit_Losses = int(budget_data[1])

    net_total = sum(Profit_Losses)
    print (f"{str(net_total)}")

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in profits (date and amount) over the entire period