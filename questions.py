import random

print("Welcome to the bank")

print("Select the option: ")
print("1 - Reserve an appointment")
print("2 - Create a new card")
print("3 - Information about the open hours of the bank")
choice = input("Enter your choice: ")
if choice == "1":
    print("What type of appointment?")
    print("a - I would like to make an investment")
if choice == "2":
    print("Credit or Debit card?")
    type = input("Enter the type of card: ")
    if type == "Credit" or "credit":
        creditCardGenerator()

def creditCardGenerator():
    number1 = random.randint(1000, 9999)
    number2 = random.randint(1000, 9999)
    number3 = random.randint(1000, 9999)
    number4 = random.randint(1000, 9999)
    number_total = str(number1) + " " + str(number2) + str(number3) + " " + str(number4)
    security_number = random.randint(100, 999)
    expiration_month = random.randint(0, 12)
    expiration_year = random.randint(0, 100)
    expiration_date = str(expiration_month) + "/" + str(expiration_year)
    print("Your credit card number: ", end=" ")
    print(number_total)
    print("Your security number: ", end= " ")
    print(security_number)
    print("The expiration date: ", end=" ")
    print(expiration_date)