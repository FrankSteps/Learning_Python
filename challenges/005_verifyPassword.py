# A password must be 8 characters long, contain 1 number, and 1 uppercase letter.

has_8char = False
has_num = False
has_Upper = False

password = input("Enter with your password: ")

# The password contain 8 characters?
if len(password) >= 8:
    has_8char = True

# The password contain a number?
# The password contain a uppercase letter?
countNum = 0
countUpper = 0

for char in password:
    if char.isdigit():
        countNum += 1
    if char.isupper():
        countUpper += 1

if countNum >= 1:
    has_num = True

if countUpper >= 1:
    has_Upper = True

# Verify and display the password security
if has_8char == True and has_num == True and has_Upper == True:
    print("Strong password")
else:
    print("Weak password")