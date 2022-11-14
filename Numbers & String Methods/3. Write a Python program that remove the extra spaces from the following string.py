#Write a Python program that remove the extra spaces from the following string:

def removewhiteSpace(userString):
    return " ".join(userString.split())
userString = input()
print(removewhiteSpace(userString))