age = int(input("Please enter your age: "))
name = input("Please enter your name: ")

if 18 <= age < 31:
    print("Have a nice holiday, {0}!".format(name))
else:
    print("You are not the right age to go on holiday!")