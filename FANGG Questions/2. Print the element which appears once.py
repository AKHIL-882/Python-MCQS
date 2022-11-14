# print the element which appears once
count=0
def singleOne(userList):
    for i in userList:
        if(userList.count(i)==1):
            print(i)
    
            
    
userList = [int(n) for n in input().split()]
singleOne(userList)