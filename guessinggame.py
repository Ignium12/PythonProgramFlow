import random

highest = 10
answer = random.randint(1,highest)
print(answer)  # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())
while guess < 1 or guess > 10:
    print("Invalid number! Please guess a number between 1 and {}: ".format(highest))
    guess = int(input())

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher!")
#     else:
#         print("Please guess lower!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
if guess == answer:
    print("You got it first time!")
while guess != answer:
    if guess < answer:
        print("Please guess higher!")
        guess = int(input())
        continue
    elif guess > answer:
        print("Please guess lower!")
        guess = int(input())
        continue

print("You got it right!")


