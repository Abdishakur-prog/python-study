# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

phone_input = input("Enter a phone number: ").strip()


if phone_input.startswith("+254"):
    phone_number = phone_input
elif phone_input.startswith("07"):
    phone_number= "+254" + phone_input[1:]
elif phone_input.startswith("7"):
    phone_number = "+254" + phone_input
elif phone_input.startswith("254"):
    phone_number = "+" + phone_input
elif phone_input.startswith("01"):
    phone_number = "+254" + phone_input[1:]
elif phone_input.startswith("1"):
    phone_number = "+254" + phone_input

if phone_number:
    print("Phone Number:", phone_number)
else:
    print("Invalid phone number format.")