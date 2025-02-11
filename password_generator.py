import random
import string
print("..... Welcome to password generator .....")
# Taking user input
alphabets = int(input("How many alphabets would you like to have in the password?\n"))
numbers = int(input("How many numbers would you like to have in the password?\n"))
special_symbols = int(input("How many special characters would you like to have in the password?\n"))
print("I will give both simple and strong passwords you can make use any one of them.\n")
# Simple password generator
simple_password = ""
for char in range(alphabets):
    simple_password += random.choice(string.ascii_letters)
for char in range(numbers):
    simple_password += random.choice(string.digits)
for char in range(special_symbols):
    simple_password += random.choice(string.punctuation)

print(f"Simple password: {simple_password}")

# Strong password generator
strong_password = []
for char in range(alphabets):
    strong_password.append(random.choice(string.ascii_letters))
for char in range(numbers):
    strong_password.append(random.choice(string.digits))
for char in range(special_symbols):
    strong_password.append(random.choice(string.punctuation))

# shuffling the list to generate random password
random.shuffle(strong_password)
password = ""
#using a for loop to traverse and append to the password
for char in strong_password:
    password += char

print(f"Strong password: {password}")
