import os
import csv

CurrDir = os.getcwd()
#print(CurrDir)

election = os.path.join("Resources", "election_data.csv")

# Lists to store data
votes = 0
numberofcandidates = 0
i = -1

#with open(election, newline='', encoding = 'utf8') as csvfile:
with open(election, newline='') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    #csvtype = type(csvreader)
    #print(csvtype)

    list1 = election[2]

    #unique candidate list
    unique_list = [] 
    votecount = []

    for row in csvreader:
        if row[2] not in unique_list: 
            unique_list.append(row[2])
            votecount.append(0)
        votes += 1
    numberofcandidates = len(unique_list)
    #print(numberofcandidates)
    #print(votecount)

    #reset csv pointer to 2nd line
    csvfile.seek(1)
    next(csvreader, None)

    for num in unique_list:
        i += 1
        #print(i)
        for rows in csvreader:
            if rows[2] == num:
                votecount[i] += 1
        csvfile.seek(1)
        next(csvreader, None)
        
    #print(votecount)
    #print(unique_list)
    #print(votes)

winner = max(votecount)
index2 = votecount.index(winner)

print()
print()
print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(votes))
print("-------------------------")
for i in unique_list:
    print(f"" + unique_list[unique_list.index(i)] + ":  " + str("{:.3%}".format(votecount[unique_list.index(i)]/votes)) + "  (" + str(votecount[unique_list.index(i)]) + ")")
print("-------------------------")
print(f"Winner:  " + unique_list[index2])
print()
print()


print("Election Results", file=open("PyPollWBS.txt", "w"))
print("-------------------------", file=open("PyPollWBS.txt", "a"))
print("Total Votes:  " + str(votes), file=open("PyPollWBS.txt", "a"))
print("-------------------------", file=open("PyPollWBS.txt", "a"))
for i in unique_list:
    print(f"" + unique_list[unique_list.index(i)] + ":  " + str("{:.3%}".format(votecount[unique_list.index(i)]/votes)) + "  (" + str(votecount[unique_list.index(i)]) + ")", file=open("PyPollWBS.txt", "a"))
print("-------------------------", file=open("PyPollWBS.txt", "a"))
print(f"Winner:  " + unique_list[index2], file=open("PyPollWBS.txt", "a"))


