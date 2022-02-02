import csv
from ipaddress import ip_address

def checkIP(str):
    try:
        ip_address(str)
        return True
    except ValueError as errorCode:
        return False



file = open('lab_assignment.csv' , 'r')
reader = csv.reader(file)
next(reader)

rows = []
public_ips = {}
for row in reader:
    rows.append(row)

for row in rows:
    if(checkIP(row[2]) and checkIP(row[3])):
        if(not(ip_address(row[2]).is_private) and ip_address(row[3]).is_private):
            if row[2] in public_ips.keys():
                public_ips[row[2]] += 1
            else:
                public_ips[row[2]] = 1

for i in public_ips:
    print(i, ":", public_ips[i])

    

