import os
import csv

#Code for the Poll

csvpath = os.path.join("Resources", "election_data.csv") 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    Candidates = [] 

    Votes_1 = 0
    Votes_2 = 0
    Votes_3 = 0

    percent_votes_1 = 0
    percent_votes_2 = 0
    percent_votes_3 = 0

    person = 0 
    ballot = 0
    TotalVotes = 0 
    
    for person in csvreader:

        if person[2] not in Candidates:
            Candidates.append(person[2])
            
    Candidate_1 = Candidates[1]
    Candidate_2 = Candidates[2]
    Candidate_3 = Candidates[3]

    print(Candidate_1,"|", Candidate_2,"|", Candidate_3)

    
    with open(csvpath, encoding='utf') as csvfile2:
        csvreader2 = csv.reader(csvfile2, delimiter=",")
        for ballot in csvreader2:
            if Candidate_1 in str(ballot):
                Votes_1 = Votes_1 + 1
            elif Candidate_2 in str(ballot):
                Votes_2 = Votes_2 + 1
            elif Candidate_3 in str(ballot):
                Votes_3 = Votes_3 + 1
    
    print(Votes_1, "|", Votes_2, "|", Votes_3)
