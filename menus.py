print("Welcome to the tip calculator.")
conta = float(input("What was the total bill?"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
total = (percentage/100) * conta / people

print(total)