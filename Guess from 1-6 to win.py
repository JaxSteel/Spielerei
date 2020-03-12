import random

user = None

computer = random.choice(["1","2","3","4","5","6"])

while user == None:
    user = input("Pick a Number from 1-6 ")
    if user not in ["1","2","3","4","5","6"]:
        print("Please pick a Number from 1-6")
        user = None

if user == computer:
    print("You Won!")
if user != computer:
    print("You Lost!")
