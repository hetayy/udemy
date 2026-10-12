# Print menu choices
list = ["1. Plan Your Week", "2. View Loaded Recipes"]

print(*list, sep='\n')

# Print selection request
menuselection = int(input("What would you like to do? "))

if menuselection == 1:
   planyourweekselection = int(input("How many days would you like to plan this week?(Default is 5 days)"))
   print(planyourweekselection)

for 