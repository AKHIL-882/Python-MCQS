
#create a Python program to sort a list in ascending order which starting from the left of the list and,compare numbers by pairs. If the first pair is ordered [smaller number, larger number], and  so on.

x = [1,2,3,4,5,7,6,8,9,10,3]
for i in range(len(x)):
    for j in range(i,len(x)):
        if(x[i]<x[j]):
            pass
        else:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
print(x)
