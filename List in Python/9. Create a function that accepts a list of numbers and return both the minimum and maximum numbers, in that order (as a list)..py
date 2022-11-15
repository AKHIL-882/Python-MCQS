
#Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).

x = [1,2,3,4,5,7,6,8,9,10,3]
print(min(x),max(x))
print()
min_ = x[0]
max_ = x[0]
for i in x:
    if(i<min_):
        min_ = i
    if(i>max_):
        max_ = i
print(min_,max_)
