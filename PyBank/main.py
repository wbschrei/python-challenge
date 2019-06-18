import os
import csv

budget = os.path.join("Resources", "budget_data.csv")

# Lists to store data
months = 0
PL = 0
DailyPL = 0
Openval = 0
Closeval = 0
AvgChange = 0
GreatIncDt = ""
GreatIncVal = 0
GreatDecDt = ""
GreatDecVal = 0

#with open(budget, newline='', encoding = 'utf8') as csvfile:
with open(budget, newline='') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        months += 1
        PL += int(row[1])
        DailyPL = (int(row[1]) - Closeval)
        if DailyPL > GreatIncVal:
            GreatIncDt = row[0]
            GreatIncVal = DailyPL
        if DailyPL < GreatDecVal:
            GreatDecDt = row[0]
            GreatDecVal = DailyPL
        if months == 1:
            Openval = int(row[1])
        Closeval = int(row[1])
    AvgChange = (PL / months)

print()
print()
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(PL))
print("Average Change: $" + str(AvgChange/months))
print(f"Greatest Increase in Profits: " + GreatIncDt + " ($" + str(GreatIncVal) + ")")
print(f"Greatest Decrease in Profits: " + GreatDecDt + " ($" + str(GreatDecVal) + ")") 
print()
print()


print("Financial Analysis", file=open("PyBankWBS.txt", "w"))
print("----------------------------", file=open("PyBankWBS.txt", "a"))
print("Total Months: " + str(months), file=open("PyBankWBS.txt", "a"))
print("Total: $" + str(PL), file=open("PyBankWBS.txt", "a"))
print("Average Change: $" + str(AvgChange/months), file=open("PyBankWBS.txt", "a"))
print(f"Greatest Increase in Profits: " + GreatIncDt + " ($" + str(GreatIncVal) + ")", file=open("PyBankWBS.txt", "a"))
print(f"Greatest Decrease in Profits: " + GreatDecDt + " ($" + str(GreatDecVal) + ")", file=open("PyBankWBS.txt", "a")) 

