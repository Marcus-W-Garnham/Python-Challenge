import os
import csv

#Code for the Poll

csvpath = os.path.join("Resources", "election_data.csv") 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    Line_count = 0
    Candidates = []

    Votes_1 = 0
    Votes_2 = 0
    Votes_3 = 0
    
    # code in between this part1 had to be done first in order to see for many candiates there were so I could code next part
    for person in csvreader:
        if person[2] not in Candidates:
            Candidates.append(person[2])
            

    #print(' | '.join(Candidates))
    #part1 end
    Candidate_1 = Candidates[1]
    Candidate_2 = Candidates[2]
    Candidate_3 = Candidates[3]
    print(Candidate_1)

    for ballot in csvreader:
        print(ballot)
        if Candidate_1 in str(ballot):
            Votes_1 == Votes_1 + 1
       
    print(' | '.join(Candidates))
    print(Votes_1)

#output to txt file using code