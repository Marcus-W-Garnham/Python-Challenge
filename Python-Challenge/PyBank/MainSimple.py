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

    print("Best Income was on the following date and was:")
    print(Entry_Date, BestIncome)
    print("Worst Income was on the following date and was:")
    print(Entry_Date_Worst, WorstIncome)
    print("The number of months this data covers is:")
    print(Months_Count)
    print("The Total Income was:")
    print(Income_Total)