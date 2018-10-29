#import the file
import os

#module for reading csv files
import csv
import pandas as pd 
import statistics
from statistics import mean
data_file = 'budget_data.csv'

csvpath = os.path.join('budget_data.csv')

totalmonths = 0
total_net = 0
runningdifference = 0

#search through file
with open(csvpath, newline='') as File:
    mylist = list(File)
    reader = csv.reader(File)
    #print the number of months
    #header = next(reader)

    firstrow = next(reader)
    #totalmonths = totalmonths + 1

    #total_net = total_net + int(firstrow[1])
    numline = len(File.readlines())
    prev_net = int(firstrow[1])
    for i in range(mylist) - 1:
        total_net = int(i[1]) - prev_net
        prev_net = int(i[1])
        runningdifference = runningdifference + total_net
        average = ((runningdifference)/len(runningdifference)  
        print(int(mylist))