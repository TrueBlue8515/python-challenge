# Import the os module
import os

# Import module for reading CSV files
import csv

Pl_list = []
date_list = []
change_list = []

# Open file to write output to
#file = open('C:\Users\halcm\Desktop\python-challenge\PyBank\PyBankResults.txt', 'w')

# Path to collect data from the Resources folder
csvpath = "Resources/budget_data.csv"

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    
    # The total number of months included in the dataset
    row_count = 0
    
    # The total net amount of "Profit/Losses" over the entire period
    total = 0

    for row in csvreader:
        total += int(row[1])
        row_count = row_count + 1
    print ("Financial Analysis")
    print ("---------------------------------------")
    print (f"Total Months : {row_count}" )
    print (f"Net Amount Profit/Losses : ${total}")

    #The average change in "Profit/Losses" between months over the entire period
    previous = 0
    current = 0
    chngPL = 0
    change = 0
    Pl_print = Pl_list

    Pl_list = int(row[1])
    date_list = row[0]
    print(f"Average Change: {Pl_list}")
    print(f"Greatest Increase in Profits: {str(date_list)}, {str(Pl_print)}")  
    print(f"Greatest Decrease in Profits: {str(date_list)}, {str(Pl_print)}")
        #change = (current - previous)
        #changelist.append(change)
        #if max < change: 
            #max = change
        #if min > change:
            #min = change
    #chngPL = sum(changelist)/len(changelist)
    #print (f"Average Change : {chngPL}")
    #print (f"Greatest Increase in Profits: {max}")
    #print (f"Greatest Decrease in Profits: {min}") 

# Output Files
#with open(file, "w") as txt_file:
	    
    #txt_file.write("Financial Analysis")
    #txt_file.write("-------------------------")
    #txt_file.write(f"Total Months : {row_count}" )
    #txt_file.write(f"Net Amount Profit/Losses : ${total}")
    #txt_file.write(f"Average Change: {Pl_list}")
    #txt_file.write(f"Greatest Increase in Profits": {str(date_list)} {str(Pl_print)}") 
    #txt_file.write(f"Greatest Decrease in Profits": {str(date_list)} {str(Pl_print)}")
    #txt_file.write("-------------------------")
	    


        


    


