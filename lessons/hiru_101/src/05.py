# Convert percentage into grade letter

# Ask student for their grade in percentage
grade = int(input("Please enter your grade (0-100)... "))

# Assign letter grade based on the percentage

'''
A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: 0 - 59
'''

if grade >= 90:
    mark = "A"

elif grade >= 80:
    mark = "B"

elif grade >= 70:
    mark = "C"

elif grade >= 60:
    mark = "D"

else:
    mark = "F"

# Print letter grade to interface

if mark == "F":
    print("Oops! Better luck next time...")
else:
    print("Well done! You earned a grade of: " + mark)
