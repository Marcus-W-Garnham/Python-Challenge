import os
import csv

#Code for the Poll

#code below is used to read from the csv file
csvpath = os.path.join("Resources", "election_data.csv") 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #After this should be able to read from the csv file

    Candidates = [] #This is also part of part one code and will be used to store the list of candidates

    #variables below were made after part1 and are used to store the votes for each of the three candidates
    Votes_1 = 0
    Votes_2 = 0
    Votes_3 = 0

    #variables below made after part1 and whill be used to store the percent of votes each candidate got
    percent_votes_1 = 0
    percent_votes_2 = 0
    percent_votes_3 = 0

    person = 0 #set to zero so when we do the in part we go through the whole csv file part1 code
    ballot = 0 #set to zero so when we do the in part we go through the whole csv file

    TotalVotes = 0 #used to store the total number of votes caste
    
    # code in between this part1 had to be done first in order to see for many candiates there were so I could code next part
    for person in csvreader:

        if person[2] not in Candidates: #checks if a candidate is already in the list and will enter the if statement if they are not in the list
            Candidates.append(person[2]) #modififes the list and adds the new canididates name to the list
            
    #place the candidates names into indibidual variables so we can use them
    Candidate_1 = Candidates[1]
    Candidate_2 = Candidates[2]
    Candidate_3 = Candidates[3]

    #print(' | '.join(Candidates)) this was the end of my part one code and it printed out all the candidates and it showed me we only had three
    print(Candidate_1,"|", Candidate_2,"|", Candidate_3) #prints candidates to the terminal

    #Need to open csv again in order to run another for loop
    with open(csvpath, encoding='utf') as csvfile2:
        csvreader2 = csv.reader(csvfile2, delimiter=",")
        for ballot in csvreader2: #run through the csv code again 
            if Candidate_1 in str(ballot): #checks if vote is for candidate 1
                Votes_1 = Votes_1 + 1 #Increases the vote count for that candidate
            elif Candidate_2 in str(ballot): #does same as above accept for candidate 2
                Votes_2 = Votes_2 + 1
            elif Candidate_3 in str(ballot): #does same as avove accept for candidate 3
                Votes_3 = Votes_3 + 1
    
    #prints the votes to the terminal
    print(Votes_1, "|", Votes_2, "|", Votes_3)

    #calculates and stores the total number of votes cast
    TotalVotes = Votes_1 + Votes_2 + Votes_3 

    #prints total votes to the terminal
    print(TotalVotes)

    #calculates percentage of the vote for each candidate to rounded to two decimal places
    percent_votes_1 = round(Votes_1/TotalVotes * 100, 2)
    percent_votes_2 = round(Votes_2/TotalVotes * 100, 2)
    percent_votes_3 = round(Votes_3/TotalVotes * 100, 2)

    #prints percent votes to the terminal
    print(percent_votes_1, "%", "|", percent_votes_2, "%", "|", percent_votes_3, "%") 

    #checks which candidate got the largest percent of the vote. Whichever Candidate has the largest percent of the vote will have there info put in new variables that will print to the text file
    if Votes_2 < Votes_1 > Votes_3:
        print("Winner is", Candidate_1, "with", percent_votes_1, "%", "of the vote.")
        Winning_Candidate = Candidate_1 
        Winning_Percent = str(percent_votes_1,)
    elif Votes_1 < Votes_2 > Votes_3:
        print("Winner is", Candidate_2, "with", percent_votes_2, "%", "of the vote.")
        Winning_Candidate = Candidate_2
        Winning_Percent = str(percent_votes_2)
    elif Votes_2 < Votes_3 > Votes_1:
        print("Winner is", Candidate_3, "with", percent_votes_3, "%", "of the vote." )
        Winning_Candidate = Candidate_3
        Winning_Percent = str(percent_votes_3)

with open("Analysis/Analysis.txt", "r+") as result: #opens text file so we can print to it
    result.write('Election Results')
    result.write('\n')
    result.write('\n')

    result.write('Total Votes: ') 
    result.write('\n')
    result.write('%d' % TotalVotes)
    result.write('\n')
    result.write('\n')

    result.write('Candidates:')
    result.write('\n')

    result.write(Candidate_1)
    result.write(' | ')
    result.write('%d' % Votes_1)
    result.write(' | ')
    result.write( str(percent_votes_1))
    result.write('%')
    result.write('\n')

    result.write(Candidate_2)
    result.write(' | ')
    result.write('%d' % Votes_2)
    result.write(' | ')
    result.write(str(percent_votes_2))
    result.write('%')
    result.write('\n')

    result.write(Candidate_3)
    result.write(' | ')
    result.write('%d' % Votes_3)
    result.write(' | ')
    result.write(str(percent_votes_3))
    result.write('%')
    result.write('\n')
    result.write('\n')

    result.write('Winner of the election is:')
    result.write('\n')
    result.write(Winning_Candidate)
    result.write(' ')
    result.write(Winning_Percent)
    result.write('%')
    
