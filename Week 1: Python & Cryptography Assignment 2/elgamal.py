import random

def check(a,b):
  t=0
  n=0
  m=0
  h=0
  j=0
  while h<a:
    j=j+h
    h=h+1
  
  while t<a-1:
    m=pow(b,t)
    n=n+(m%a)
    t=t+1
  
  if n==j:
    return True
  return False  
    
def prime(x):
   t=2
   while t<x:
     if x%t==0:
       return False
     t=t+1
     return True
     
p=random.randint(0,100)
while True:
 p=random.randint(0,100)
 if prime(p):
   break
al=1
while al<p:
  if check(p,al):
    break
  al=al+1  
a=random.randint(2,(p-1))
print("private key ",a)
w=pow(al,a)
q=w%p
print("public key ",p,",",w,",",q)

