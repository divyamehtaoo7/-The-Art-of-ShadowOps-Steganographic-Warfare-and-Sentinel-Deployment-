import random
def prime(x):
   t=2
   while t<x:
     if x%t==0:
       return False
     t=t+1
   return True

p=2
q=2

while True :
  p=random.randint(10,200)
  q=random.randint(10,200)
  if(prime(p) and prime(q) and p!=q):
     break
n=p*q
g=n+1
print("public key is",n,",",n+1)
w=(p-1)*(q-1)
t=0
while (n*t+1)%w !=0:
  t=t+1
print("private key",n,",",w,",",(n*t+1)/w )  
