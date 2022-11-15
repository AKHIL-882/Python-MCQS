
#Create a Python program that takes a number and returns a list with the digits of the number in reverse order
x = []
userValue = input()
reverseUserValue = userValue[::-1]
print(list(reverseUserValue))

def reverse_list(num):
    return [int(i) for i in str(num)[::-1]]