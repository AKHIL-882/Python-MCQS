
#Write a Python program that complete an array with random numbers
x = []
import random
for i in range(1,10):
    values = random.randint(1,10)
    x.append(values)

print(x)
