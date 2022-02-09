def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def phi_1(n):
    list1 = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            list1.append(i)
    return list1

if __name__ == '__main__':
    print("7/3 = ",7/3)
    print("7//3 = " ,7//3)
    print("GCD: " ,gcd(12,6))
    
    #lambda is an anonymous function, here phi will be a function
    phi = lambda n: [i for i in range(1,n) if gcd(i, n) == 1]  
    print("phi", phi)
    print("List returned by phi(26): ", phi(26), "Length of list: ", len(phi(26)))
    print("List returned by phi_1(26): ", phi_1(26), "Length of list: ", len(phi_1(26)))

    #function to calculate modular multiplicative inverse of given number under modulo 26
    modulo_inverse = lambda n: [i for i in range(1, 26) if(n * i) % 26 == 1]
    print("multiplicative inverse of 15 modulo 26: ", modulo_inverse(15))