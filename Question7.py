# Write a Python Program to check the validity of a password (input from users)

# Validation :
#     At least 1 letter between [a-z] and 1 letter between [A-Z]
#     At least 1 number between [0-9]
#     At least 1 character from [$#@]
#     Minimum length 6 characters
#     Maximum length 16 characters

userPassword = input("Enter Your Own Password\n")

countOfAlphabets = 0
countOfNumbers = 0
countOfSpecials = 0

lengthOfPassword = len(userPassword)

if 6 < lengthOfPassword < 16:
    print(f"Length Of Password Is {lengthOfPassword}")
    for ch in userPassword:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            countOfAlphabets = countOfAlphabets + 1
        elif '0' <= ch <= '9':
            countOfNumbers = countOfNumbers + 1
        else:
            if ch == "$" or ch == "#" or ch == "@":
                countOfSpecials = countOfSpecials + 1
else:
    print(" Password Out Of Range (6,16) ")

if countOfNumbers >= 1 and countOfSpecials >= 1 and countOfAlphabets >= 1:
    print("Password Validated Successfully")
else:
    print("Password Validation Unsuccessfully")
