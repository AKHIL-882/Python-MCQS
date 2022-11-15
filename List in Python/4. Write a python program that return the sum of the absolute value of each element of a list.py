
#Write a python program that return the sum of the absolute value of each element of a list 
def absoluteSum(x):
    return abs(sum(x))
    # return sum(map(abs, x))

x = [1,2,3,4,5,6,7,8,9,10]
print(absoluteSum(x))
