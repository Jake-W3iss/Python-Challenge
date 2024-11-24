# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
previousNet = 0
curretNet = 0
months =[]
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
 
    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    firstRow = next(reader)
    total_months += 1
    total_net = float(firstRow[1])
    print(total_net)
    # Track the total and net change
    previousNet = float(firstRow[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months +=1
        total_net = total_net+ float(row[1])
        #print(total_net)
        # Track the net change
            #profits and losses in index 1
        netChange = float(row[1])- previousNet
        net_change_list.append(netChange)

        previousNet = float(row[1])
    
        months.append(row[0])

        



# Calculate the average net change across the months
averageNetChange = sum(net_change_list)/len(net_change_list)

GreatestInc = [months[0], net_change_list[0]]
GreatestDec = [months[0], net_change_list[0]]

for m in range(len(months)):
    if(net_change_list[m] > GreatestInc[1]):
        GreatestInc[1] = net_change_list[m]
        GreatestInc[0] = months[m]
    if(net_change_list[m] < GreatestDec[1]):
        GreatestDec[1] = net_change_list[m]
        GreatestDec[0] = months[m]

# Generate the output summary
output = ( 
    f"Financial Analysis \n"
    f"\n"
    f"-------------------- \n"
    f"\n"
    f"Total Months = {total_months} \n" 
    f"\n"
    f"Total = ${total_net:,.2f} \n"
    f"\n"
    f"Average Change = ${averageNetChange:,.2f}\n"
    f"\n"
    f"Greatest Increase in Profit: {GreatestInc[0]} (${GreatestInc[1]:,.2f})\n"
    f"\n"
    f"Greatest Loss in Profit: {GreatestDec[0]} $({GreatestDec[1]:,.2f})\n"
    )



# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
