# This program calculates prices for custom house signs.

charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"
charge = 35

numChars = int(input("Please select number of characters: "))
woodType = input("Please select a wood type between (oak or pine): ")
color = input("Please select between the character colors (gold or black): ")

if numChars > 5:
    charge += (numChars -5) * 4

if woodType == "oak":
    charge += 20

if color =="gold":
    charge += 15
    
print(f"The charge for this sign is ${charge: }")