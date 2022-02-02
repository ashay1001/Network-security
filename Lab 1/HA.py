import math

const = (math.sqrt(8))/9801
value = 0
k = 0
counter = 100

while(counter > k):
    value += const*(math.factorial(4*k)/pow(math.factorial(k),4))*((26390*k+1103)/pow(396,4*k))
    k += 1

print("Value of pi: ", 1/value)