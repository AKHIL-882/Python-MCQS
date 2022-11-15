
#Write a Python program that accepts a list and returns the last item in the list
def returnLastItem(x):
    return x[-1]
    # return sum(map(abs, x))

x = [1,2,3,4,5,6,7,8,9,10,'a','b']
print(returnLastItem(x))
