import random
def coprime(a,b):
  w=b
  while w>1:
    if a%w==0 and b%w==0:
      return False
    w=w-1 
    
  return True
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
  p=random.randint(10,300)
  q=random.randint(10,300)
  if(prime(p) and prime(q) and p!=q):
     break
n=p*q
w=(p-1)*(q-1)
print(w)
while True:
  e=random.randint(1,100)
  if coprime(w,e):
    break
print("public key is",n,",",e)
t=0
while True:
  if (w*t+1)%e==0:
    break
  t=t+1

print("private key is ",n,",",(w*t+1)/e)
