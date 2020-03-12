import random
import string

user_choice = None

while user_choice == None:   
    try:
        user_choice = int(input("Please choose the length of the password? "))
        if user_choice < 6:
            print("Please at least 6 characters")
            user_choice = None
    except ValueError:
        user_choice = none

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(1,user_choice+1))
print("Your password is{}".format(password))