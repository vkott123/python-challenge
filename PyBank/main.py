#Python Homework
#Submitted By: Veena Kottoor

import os
import csv

# Joining path where the csv file is located
budget_data = os.path.join("budget_data.csv")

# Open/Read the csv file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Calculate the total number of months 
    # Calculate the net total amount of "Profit/Losess"
    
    P = []
    months = []

    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    total_months = len(months)

    # Calculate the average change in "Profit/Losses"
    data_change = []

    for x in range(1, len(P)):
        data_change.append((int(P[x]) - int(P[x-1])))
    
    # calculate average revenue change
    average_change = sum(data_change) / len(data_change)

     # Round average change to two decimal points
    average_change = round(average_change,2)
    

    # Calculate the greatest increase in profits
    greatest_increase = max(data_change)

    # Calculate greatest decrease in losses
    greatest_decrease = min(data_change)

    # Print the analysis to the terminal

    print("\nFinancial Analysis")

    print("----------------------------")

    print("Total Months: " + str(total_months))

    print("Total: " + "$" + str(sum(P)))

    print("Average Change: " + "$" + str(average_change))

    print("Greatest Increase in Profits: " + str(months[data_change.index(max(data_change))+1]) + " " + "(" + "$" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months[data_change.index(min(data_change))+1]) + " " + "(" + "$" + str(greatest_decrease) + ")")


    # Export a text file with the results

    file = open("Financial Analysis.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("----------------------------" + "\n")

    file.write("Total Months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average Change: " + "$" + str(average_change) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[data_change.index(max(data_change))+1]) + " " + "(" + "$" + str(greatest_increase) + ")" + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[data_change.index(min(data_change))+1]) + " " + "(" + "$" + str(greatest_decrease) + ")" + "\n")

    