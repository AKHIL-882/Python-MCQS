# Write a Python program that Create a function that gives True if a string is empty and False otherwise.
def isFunctionEmpty(userString):
    if(userString == ""):
        return True
    else:
        return False
userString = input()
print(isFunctionEmpty(userString))


def empty(st):
    return not st
print(empty(''))
print(empty('   5gh'))