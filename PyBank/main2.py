import os
import csv

cash_csv = os.path.join('..','Resources','budget_data.csv')

with open(cash_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip headers when counting data
    csv_header = next(csvfile)
    
    all_months = []
    all_profits = []

    for row in csvreader:
        months = row[0]
        profits = int(row[1])
        all_months.append(months)
        all_profits.append(profits)

# What will the print report look like?
print("Financial Analysis")
print("----------------------------")
# How to print count of total months and total $$$
print("Total Months: " + str(len(all_months)))
print("Total: $" + str(sum(all_profits)))
# How to find average
# NEEEED HEEEELLLPPP
# How to find greatest increase and decrease
max = max(all_profits)
min = min(all_profits)
print("Greatest Increase in Profits: " + "($" + str(max) + ")")
print("Greatest Decrease in Profits: " + "($" + str(min) + ")")