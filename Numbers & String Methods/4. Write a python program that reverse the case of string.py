# Write a python program that reverse the case of string

def caseChange(userString):
    res = ""
    for i in userString:
        if(i.isupper()):
            res = res +  i.lower()
        else:
            res = res + i.upper()
    return res
    
userString = input()
print(caseChange(userString))
            
###########################################
s = "I am a python developer"
def reverse_case(s):
    return s.swapcase()

print(reverse_case("I am a python developer"))