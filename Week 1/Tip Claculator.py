print("Hello! Welcome to the Tip Calculator."
      "Here, you will input your bill amount, the tip % and the # of people"
      "and the program will accurately tell you who owes what...Ready?")

bill = int(input("Please enter the total bill amount: "))

per = float(input("Please enter the tip %: "))

ppl = int(input("Please enter the # of people: "))

tip_amt = (bill*(per/100))

personal_tip = (tip_amt/ppl)

print(f"According to the system, each of the {ppl} people, owes CAD ${personal_tip}")