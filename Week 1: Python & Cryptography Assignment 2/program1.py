def encrypt(letter,k):
  y=list(letter)
  x=[]
  ans=""
  for i in range(len(y)):
    m=ord(y[i])
    m=m-97+k
    m=m%26
    m=m+97
    x.append(chr(m))
  print(ans.join(x))
  print(len(ans.join(x)))

def decrypt(letter,k):
   y=list(letter)
   x=[]
   ans=""
   for i in range(len(y)):
      m=ord(y[i])
      m=m-97-k+26
      m=m%26
      m=m+97
      x.append(chr(m))
   print(ans.join(x))
   print(len(ans.join(x)))

letter=input("string:"  )
n=int(input("key:"   ))
k=n%26
w=input("e or d:"   )
if w=="e":
 encrypt(letter,k)
elif w=="d":
 decrypt(letter,k)
