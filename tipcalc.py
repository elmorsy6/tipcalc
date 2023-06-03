print("Welcome to tip calculator: ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
# totalBill With FinalTip
totalBill = totalTipAmount + bill
# division bill on people will buy
billPerPerson = totalBill / people
# finalAmount = round(billPerPerson, 2)
finalAmount = "{:.2f}".format(billPerPerson)
print(f"Each Person Should Pay ${finalAmount}")