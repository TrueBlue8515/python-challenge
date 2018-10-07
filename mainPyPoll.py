#Import the os module
import os

# Import module for reading CSV files
import csv

import collections as ct

# Open file to write output to
#file = open('C:\Users\halcm\Desktop\python-challenge\PyPoll\PyPollResults.txt', 'w')

# Path to collect data from the Resources folder
csvpath = "election_data.csv"

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    
    #The total number of months included in the dataset
    row_count = 0

#The total number of votes cast
    for row in csvreader:
        row_count = row_count + 1

#A complete list of candidates who received votes  
    votes = ct.Counter()
    candidate = []
 
    for row in csvreader:
        candidate = int(row[2])
        votes[candidate] += 1
    
print ("Election Results")
print ("---------------------------------------")
print (f"Total Votes: {row_count}")
print ("---------------------------------------")
print (votes)
print ("---------------------------------------")
print (f"Winner: ")
print ("---------------------------------------")

# Output Files
#with open(file, "w") as txt_file:
	    
    #txt_file.write("Election Results")
    #txt_file.write("---------------------------------------")
    #txt_file.write(f"Total Votes: {row_count}")
    #txt_file.write("---------------------------------------")
    #txt_file.write(votes)
    #txt_file.write("---------------------------------------")
    #txt_file.write(f"Winner: ")
    #txt_file.write("---------------------------------------")