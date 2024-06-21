p=int(input("prime number "))
al=int(input("primitive root of prime number "))
a=int(input("integer less than prime number "))
print("private key ",a)
w=pow(al,a)
q=w%p
print("public key ",p,",",w,",",q)

