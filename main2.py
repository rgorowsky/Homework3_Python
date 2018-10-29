#import the file
import os

#module for reading csv files
import csv
import pandas as pd 
import statistics

#open file
data_file = 'budget_data.csv'
csvpath = os.path.join('budget_data.csv')
data_file_pd = pd.read_csv(data_file)

#search through file
with open(csvpath, newline='') as File:
    #don't know if the below line is needed
    reader = csv.reader(File)
    numline = len(File.readlines())

    #print the number of months
    print("There are " + str(numline) + " months included in the dataset")

    #print the sum total of profits/losses
    total = data_file_pd["Profit/Losses"].sum()
    print("Total Profits And/Or Losses in the period: " + str(total))

    #create a new column to see if that helps me
    firstrow = next(reader)
    prev_net = int(firstrow[1])
    for i in range(mylist) - 1:
        prev_net = int(i[1])
        total_net = int(i[1]) - prev_net
        runningdifference = runningdifference + total_net
        next(i)
            average = ((runningdifference)/len(runningdifference)  
            print(average)
   