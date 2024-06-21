def gcd_on(a,b):
  w=b
  while w>0:
    if a%w==0 and b%w==0:
      return w

    w=w-1  
def gcd_euclidean(a,b):
  if a%b==0:
    return b
  t=0  
  t=b
  b=a%b
  a=t
  return gcd_euclidean(a,b)
a=int(input("enter a number  "))
b=int(input("enter another number "))

if a<b :
   t=0
   t=b
   b=a
   a=t
if a>b:
  print(gcd_on(a,b))
  print(gcd_euclidean(a,b))

