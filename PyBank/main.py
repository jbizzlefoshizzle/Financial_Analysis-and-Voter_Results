# default declarations for
# importing csv file
import os
import csv

# Dude, Where's my [csv file]?
cash_csv = os.path.join('..','Resources','budget_data.csv')

# What function we using?
# What parameter we using?
def print_analysis(csv_data):
    # Assign values to variables, yo
    date = str(csv_data[0])
    money = int(csv_data[1])

    # Total months
    #all_months = []

# Read in the csv file
with open(cash_csv,'r') as csvfile:

    # Split csv data by comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # do not print the header
    header = next(csvreader)