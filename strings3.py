# number = "9,223;273:036 854,775;807"
number = input("Please enter a series of numbers, using any seperators you like: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)