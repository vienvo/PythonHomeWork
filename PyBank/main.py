#Import dependencies
import os
import csv

# Setup path
bugetCSV = os.path.join("..","PyBank","budget_data.csv")

# Create list to hold values
profits = []
changes = []
months = []

# Open the budget file
with open(bugetCSV,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    totalMonth = 0
    total = 0

    # Loop file to get total, months, and list of profits & months
    for row in csvreader:
        total = total + float(row[1])
        totalMonth += 1
        profits.append(row[1])
        months.append(row[0])

# Loop to get changes in profit month-over-month
for a, b in zip(profits[::1], profits[1::1]):
    change = int(b) - int(a)
    changes.append(change)

# Variable to determine max/min change in profit and its position
maxChange = max(changes)
minChange = min(changes)
maxMonth = changes.index(maxChange) + 1
minMonth = changes.index(minChange) + 1

# Return results to terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Month: {int(totalMonth)}')
print(f'Total: ${int(total)}')
print(f'Average Change: ${round(sum(changes)/len(changes),2)}')
print(f'Greatest Increase in Profits: {months[maxMonth]} (${maxChange})')
print(f'Greatest Decrease in Profits: {months[minMonth]} (${minChange})')

# Return results to output text file
with open('pyBank_output.csv','w',newline='') as csvOutput:
    csvwriter = csv.writer(csvOutput,delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Month: ', int(totalMonth)])
    csvwriter.writerow(['Total: ', int(total)])
    csvwriter.writerow(['Average Change: ', round(sum(changes)/len(changes),2)])
    csvwriter.writerow(['Greatest Increase in Profits: ', months[maxMonth], maxChange])
    csvwriter.writerow(['Greatest Decrease in Profits: ', months[minMonth], minChange])