def encrypt(letter,k):
  y=list(letter)
  x=[]
  ans=""
  for i in range(len(y)):
    if y[i]==" " or y[i]=="." or y[i]=="," or y[i]=="!" or y[i]=="?":
      x.append(y[i])
      continue;
    m=ord(y[i])
    m=m-97+k
    m=m%26
    m=m+97
    x.append(chr(m))

  with open("output.txt","w") as f:
    f.write(ans.join(x))

def decrypt(letter,k):
   y=list(letter)
   x=[]
   ans=""
   for i in range(len(y)):
      if y[i]==" " or y[i]=="." or y[i]=="," or y[i]=="!" or y[i]=="?":
        x.append(y[i])
        continue;
      m=ord(y[i])
      m=m-97-k+26
      m=m%26
      m=m+97
      x.append(chr(m))

   with open("output.txt","w") as f:
     f.write(ans.join(x))

file=input("file location  "  )
with open(file,"r") as f:
 letter=f.read()

n=int(input("key:"   ))
k=n%26
w=input("e or d:"   )
if w=="e":
 encrypt(letter,k)
elif w=="d":
  decrypt(letter,k)