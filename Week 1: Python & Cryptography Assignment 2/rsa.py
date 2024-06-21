import random
def prime(x):
   t=1
   while t<x:
     if x%t==0:
       return False
     t=t+1
  return true
p=0
q=0
while !(prime(P) && prime(Q) && p==q) :
  p=random.randint(0,1000)
  q=random.randint(0,1000)
n=p*q
e=int(input("enter encryptio exponent "))
print("public key is",n,",",e)
w=(p-1)*(q-1)
t=0
while (w*t+1)%e!=0:
  t=t+1
print("private key is ",n,",",(w*t+1)/e)
