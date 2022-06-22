import os
import csv
import math

#Code for the bank

csvpath = os.path.join("Resources", "budget_data.csv") 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    BestIncome = -math.inf
    WorstIncome = math.inf
    Line_count = 0
    Months_Count = 0
    Income = 0
    Income_Total = 0
    Income_Average = 0
    #change from month to month then use to calculate for entire time span

    for row in csvreader:

        if Line_count == 0:
            Line_count += 1

        else:
            Income = float(row[1])
            Income_Total += Income
            Months_Count += 1
            if Income > BestIncome:
                Entry_Date = row[0]
                BestIncome = float(row[1])
            elif Income < WorstIncome:
                Entry_Date_Worst = row[0]
                WorstIncome = float(row[1])
            else:
                Income = float(row[1]) 

with open(csvpath, encoding='utf') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=",")

    switch = 0
    switch2 = 0
    count_changes = 0
    Total_change = 0
    for change in csvreader2:
        if switch == 0:
            switch = 1
        else:
            new = float(change[1])
            if switch2 == 0:
                switch2 = 1
                old = float(change[1])
            else:
                change = new - old
                old = new
                Total_change = Total_change + change
                count_changes = count_changes + 1

    Average_change = round(Total_change/count_changes, 2)       
    print("Best Income was on the following date and was:")
    print(Entry_Date, BestIncome)
    print("Worst Income was on the following date and was:")
    print(Entry_Date_Worst, WorstIncome)
    print("The number of months this data covers is:")
    print(Months_Count)
    print("The Total Income was:")
    print(Income_Total)
    print(count_changes)
    print(Average_change)

    with open("Analysis/Analysis.txt", "r+") as result: #opens text file so we can print to it
        result.write('Financial Analysis')
        result.write('\n')

        result.write('Total Months: ')
        result.write(str(Months_Count))
        result.write('\n')

        result.write('Total: ')
        result.write(str(Income_Total))
        result.write('\n')

        result.write('Average Change: ')
        result.write(str(Average_change))
        result.write('\n')

        result.write('Greatest Increase in Profits: ')
        result.write(Entry_Date)
        result.write(' ')
        result.write(str(BestIncome))
        result.write('\n')

        result.write('Greatest Decrease in Profits: ')
        result.write(Entry_Date_Worst)
        result.write(' ')
        result.write(str(WorstIncome))
        result.write('\n')