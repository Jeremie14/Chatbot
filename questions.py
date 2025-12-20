import random
import time

def creditCardGenerator():
    number1 = random.randint(1000, 9999)
    number2 = random.randint(1000, 9999)
    number3 = random.randint(1000, 9999)
    number4 = random.randint(1000, 9999)
    number_total = str(number1) + " " + str(number2) + " " + str(number3) + " " + str(number4)
    security_number = random.randint(100, 999)
    expiration_month = random.randint(1, 12)
    expiration_year = random.randint(1, 100)
    expiration_date = str(expiration_month) + "/" + str(expiration_year)
    print("Your credit card number: ", end=" ")
    print(number_total)
    print("Your security number: ", end= " ")
    print(security_number)
    print("The expiration date: ", end=" ")
    print(expiration_date)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print(creditCardGenerator())
    

print("Welcome to the bank!")

print("Select the option: ")
print("1 - Reserve an appointment")
print("2 - Create a new card")
print("3 - Information about the open hours of the bank")

choice = int(input("Enter the number of your choice: "))
if choice not in (1, 2, 3):
    raise Exception("Insert a valid choice!")


if choice == 1:
    print("What type of appointment?")
    print("A - I would like to make an investment")
    print("B - I need some advices")
    type_of_appoint = input("Enter the type of appointment: ")
    if type_of_appoint not in ("A", "B"):
        raise Exception("Insert a valid choice!")
    if type_of_appoint == "A":
        print("In what would you like to invest?")
        print("a - Nasdaq")
        print("b - S&P500")
        type_of_invest = input("Enter: ")
        if type_of_invest not in("a", "b"):
            raise Exception("Insert a valid choice!")
        print("How much would you like to invest?")
        quantity_money = input("Enter: ")
        print(f"Congratulations you have invested {quantity_money} in  the {type_of_invest}!")

    if type_of_appoint == "B":
        print("For more information, please take a look at our new website")


if choice == 2:
    print("Credit or Debit card?")
    type = input("Enter the type of card(Credit/Debit): ")
    if type not in ("Credit", "Debit"):
        raise Exception("Insert a valid choice!")
    if type == "Credit":
        print("Your card is in processs of being created")
        print(countdown(10))
    elif type == "Debit":
        print("Perfect, your card just got created. You can come pick it up!")

if choice == 3:
    print("We are open from Monday to Friday from 8am to 8pm!")