p=int(input("frist prime number "))
q=int(input("second prime number  "))
n=p*q
g=n+1
print("public key is",n,",",n+1)
w=(p-1)*(q-1)
t=0
while (n*t+1)%w !=0:
  t=t+1
print("private key",n,",",w,",",(n*t+1)/w )  


