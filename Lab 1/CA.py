def printPattern(n):
  for i in range(n):
    midVal = int(n/2)
    for j in range(n):
        if (i == 0 or i == midVal or i == n-1):
            print("-", end=" ")
        elif (j == 0 or j == midVal or j == n-1):
            print("|", end=" ")
        else: 
            print(" ", end=" ")
    print()

n = int(input("Enter the number: "))
printPattern(n)