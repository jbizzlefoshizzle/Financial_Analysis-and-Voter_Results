# default declarations for
# importing csv file
import os
import csv

# Dude, Where's my [csv file]?
cash_csv = os.path.join('..','Resources','budget_data.csv')

# Lists to store data, y'all
all_months = []
all_profits = []

# What function we using?
# What parameter we using?
def print_analysis(csv_data):
    # Assign values to variables, yo
    date = str(csv_data[0])
    money = int(csv_data[1])

# Read in the csv file
with open(cash_csv,'r') as csvfile:

    # Split csv data by comma
    csvreader = csv.reader(csvfile, delimiter=',')
    # Alright, what meow?
    for row in csvreader:
        # Add month to month list
        all_months.append(row[0])
        # TEST LINE!!!
        print(all_months)

        # Add profit to profits list
        # all_profits.append(row[1])

    # do not print the header
    header = next(csvreader)

# Set variable for output file
#--> output_file = os.path.join("financial_analsis.txt")
