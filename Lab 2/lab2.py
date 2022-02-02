str1 = "Hello World"
print('Hel' in str1)
print("Hel" in str1)
print("hel" in str1)

list1 = [1,22,34,55,67,70]
print(23 in list1)
print(22 in list1)

str2 = "ABC"
list2 = [100,200,300]

for (a, b) in enumerate(zip(list1, str1)):
    print(a, b)

print("list1: ", list1)
print("list2", list2)

list1.extend(list2)
print(list1)

#--------------- file handling -----------

import os
cwd = os.getcwd()
print("\nCurrent Working Directory is: ", cwd)

file1 = open('sample.txt', 'r')

list3 = file1.read().split()

print(list3)


