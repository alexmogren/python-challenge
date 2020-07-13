#Import Resource Data
import os
import csv

date = []
profits_losses = []
total_months = 0
month_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0


#Directory
csvpath = os.path.join('Resources1', 'budget_data.csv')
# Read Header Row First
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    header = next(csvreader)

    # Extract First Row From List
    first_row = next(csvreader)
    total_months = total_months + 1
    total_revenue = total_revenue + int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        # Calculate Number of Months
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        # Calculate Net Change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_change = month_change + [row[0]]
        # Calculate the Greatest Increase in Revenue
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the Greatest Decrease in Revenue
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
# Calculate the Average Net Change Per Month
    net_monthly_avg = sum(net_change_list) / len(net_change_list)


#Print Results
print("Financial Analysis")
print("----------------------")
print("Total Months:" + str(total_months))
print("Total Revenue:" + str(total_revenue))
print("Average Revenue Change:" + str(net_monthly_avg))
print("Greatest Increase in Profit:" + str(greatest_increase[0]) + "($ " + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profit:" + str(greatest_decrease[0]) + "($ " + str(greatest_decrease[1]) + ")")

#Output of Results
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average  Change: ${net_change_list:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Export File

with open("financial_analysis.txt", "w") as txt_file:
    txt_file.write(output)
    