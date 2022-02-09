def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def mod_inv(a, m):
    for i in range(1, m):
        if(a * i) % m == 1:
            return i

def crt():
    n = int(input("Enter the number of equations: "))
    list1 = []
    list2 = []
    print("Enter a1, a2, a3, ... an")
    for i in range(0, n):
        list1.append(int(input()))
    
    print("Enter p1, p2, p3, ... pn")
    for i in range(0, n):
        list2.append(int(input()))

    #--------- step 1------------------
    M = 1
    for i in range(0, n):
        M = M * list2[i]
    print("\nStep 1: M = ", M)
    
    #--------- step 2------------------
    list3 = []
    for i in range(0, n):
        list3.append(M//list2[i])
    
    print("\nStep 2: M1, M2, M3....Mn")
    print(list3)
    
    #--------- step 3------------------
    list4 = []
    for i in range(0, n):
        t = mod_inv(list3[i], list2[i]);
        list4.append(t)
    
    print("\nStep 3: inverse (M1), inverse (M2), inverse (M3)....inverse (Mn)")
    print(list4)

    #--------- step 4------------------
    X = 0
    for i in range(0, n):
        X = (X + list1[i]*list3[i]*list4[i])
    
    print("\nStep 4: X = ", X, " (mod", M ,")")
    print("X = ", X%M)


if __name__ == "__main__":
    crt()