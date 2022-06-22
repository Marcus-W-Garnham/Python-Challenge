import os
import csv
import math

#Code for the bank

#open csv path
csvpath = os.path.join("Resources", "budget_data.csv") 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    BestIncome = -math.inf #sets best income to a infinite negative 
    WorstIncome = math.inf #sets worst income to infinite positive 
    Line_count = 0
    Months_Count = 0
    Income = 0
    Income_Total = 0
    Income_Average = 0
    
    #this part of the code is used to find biggest increase and decrease and count the rows that actually have numbers in them
    for row in csvreader:

        if Line_count == 0: #used to skip the top row as those are just column headers
            Line_count += 1

        else:
            Income = float(row[1]) #places income into a variable
            Income_Total += Income
            Months_Count += 1
            if Income > BestIncome: #checks if its variable we just got is higher than what is inside best income. always true first time since its infinite negative
                Entry_Date = row[0] #gets entry date for new best income
                BestIncome = float(row[1]) #gets the new best income
            elif Income < WorstIncome: #checks if new variable we just got is lower than what is already in worst income. always true first time as it was infinite positive.
                Entry_Date_Worst = row[0] #update worst entry date
                WorstIncome = float(row[1]) #update new worst income
            else:
                Income = float(row[1]) #need to do something in the else

#need to open the csv file again in order to use it
with open(csvpath, encoding='utf') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=",")

    #callculate change from month to month then use to calculate for entire time span
    switch = 0
    count_changes = 0
    Total_change = 0
    for change in csvreader2:
        if switch == 0: #need this part to skip the top row with column names
            switch = 1
        else:
            new = float(change[1]) #get the income value
            if switch2 == 0: #enters only once and we need this for when we only have are first value
                switch2 = 1
                old = float(change[1])
            else: #this section is used to calculate are change in porjits for each month then puts that in a total
                change = new - old
                old = new
                Total_change = Total_change + change
                count_changes = count_changes + 1

    Average_change = round(Total_change/count_changes, 2)  #gets the average change in our profit     
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

    with open("Analysis/Analysis.txt", "r+") as result: #opens text file so we can print results to it
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