p=int(input("frist prime number "))
q=int(input("second prime number  "))
n=p*q
e=int(input("enter encryptio exponent "))
print("public key is",n,",",e)
w=(p-1)*(q-1)
t=0
while (w*t+1)%e!=0:
  t=t+1
print("private key is ",n,",",(w*t+1)/e)
