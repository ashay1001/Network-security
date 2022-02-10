def modulo_inv(a, m) : 
    number = m 
    t1 = 0
    t2 = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
 
        quotient = a // m 
        temp = m 
   
        m = a % m 
        a = temp 
        temp = t1 
 
        t1 = t2 - quotient * t1 
        t2 = temp 
   
    if (t2 < 0) : 
        t2 = t2 + number 
  
    return t2 
  
  
if __name__ == '__main__': 
    a = int(input("Enter value of a: "))
    m = int(input("Enter value of m: "))
    print("Required Inverse is: ", modulo_inv(a, m)) 