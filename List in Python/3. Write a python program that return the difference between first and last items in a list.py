
#Write a python program that return the difference between first and last items in a list
def firstAndLastDiff(x):
    return x[0]-x[len(x)-1]

x = [1,2,3,4,5,6,7,8,9,10]
print(firstAndLastDiff(x))
