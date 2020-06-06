# Declarations
import os
import csv
#NEED THIS TO CALCULATE DIFFERENCES BETWEEN MONTHS
import numpy as np

# Show me the money
cash_csv = os.path.join('..','Resources','budget_data.csv')
# Open and Read
with open(cash_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip headers when counting data
    csv_header = next(csvfile)
    # Empty lists 
    all_months = []
    all_profits = []
    # Put stuff in lists
    for row in csvreader:
        months = row[0]
        profits = int(row[1])
        all_months.append(months)
        all_profits.append(profits)
        # Month of max/min
        big_money = max(all_profits)
        lose_money = min(all_profits)
        if row[1] == str(lose_money):
            lose_money_day = row[0]
        if row[1] == str(big_money):
            big_money_day = row[0]
            
# What will the terminal report look like?
print("Financial Analysis")
print("----------------------------")
# How to print count of total months and total $$$
print("Total Months: " + str(len(all_months)))
print("Total: $" + str(sum(all_profits)))

# Create list of changes between months
monthly_changes = np.diff(all_profits)
# How to find average
average = sum(monthly_changes)/len(monthly_changes)
average_dollars = format(average,'.2f')
print("Average Change: $" + str(average_dollars))

# How to find greatest increase and decrease
max = max(monthly_changes)
min = min(monthly_changes)
print("Greatest Increase in Profits: " + str(big_money_day) + " ($" + str(max) + ")")
print("Greatest Decrease in Profits: " + str(lose_money_day) + " ($" + str(min) + ")")

# What will the text output look like?
p = open("Financial_Analysis.txt", "a")
print("Financial Analysis", file=p)
print("----------------------------", file=p)
print("Total Months: " + str(len(all_months)), file=p)
print("Total: $" + str(sum(all_profits)), file=p)
print("Average Change: $" + str(average_dollars), file=p)
print("Greatest Increase in Profits: " + str(big_money_day) + " ($" + str(max) + ")", file=p)
print("Greatest Decrease in Profits: " + str(lose_money_day) + " ($" + str(min) + ")", file=p)