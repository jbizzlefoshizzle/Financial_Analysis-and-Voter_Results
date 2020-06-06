# Declarations
import os
import csv
#NEED THIS TO CALCULATE DIFFERENCES BETWEEN MONTHS
import numpy as np

# Defining max and min functions
# -------------------------------------
def max(array, n):
    
    max = array[0]
    
    for i  in range (1, n):
        if array[i] > max:
            max = array[i]
    return max
# -------------------------------------
def min(array, n):
    
    min = array[0]
    
    for i  in range (1, n):
        if array[i] < min:
            min = array[i]
    return min

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
        
#         Months of largest profit/loss
        
        n = len(all_profits)
        biggest_profit = max(all_profits, n)
        biggest_loss = min(all_profits, n)
        
        if row[1] == str(biggest_profit):
            big_profit_month = row[0]
        if row[1] == str(biggest_loss):
            big_loss_month = row[0]

# Create list of changes between months
monthly_changes = np.diff(all_profits)
# How to find average
average = sum(monthly_changes)/len(monthly_changes)
average_change = format(average,'.2f')

m = len(monthly_changes)
greatest_increase = max(monthly_changes, m)
greatest_loss = min(monthly_changes, m)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(all_months)))
print("Total: $" + str(sum(all_profits)))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(big_profit_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(big_loss_month) + " ($" + str(greatest_loss) + ")")