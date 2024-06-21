def gcd_exeuc(a,b):
  x1 = 1
  y1 = 0
  z1 = a
  x2 = 0
  y2 = 1
  z2 = b
  while z2 != 0:
      m = z1//z2
      x3 = x1 - m*x2
      y3 = y1 - m*y2
      z3 = z1 - m*z2
      x1 = x2
      y1 = y2
      z1 = z2
      x2 = x3
      y2 = y3
      z2 = z3
  return [x1, y1, z1]
A=int(input("frist number  ")) 
B=int(input("second number  "))
C=int(input("third number  ")) 
D=int(input("fourth number  "))
w=gcd_exeuc(A,B)
k=gcd_exeuc(C,w[2])
if D%k[2]!=0:
    print("no solution")
if D%k[2]==0:
    print("a  ",w[0]*k[1]*D/k[2])
    print("b  ",w[1]*k[1]*D/k[2])
    print("c  ",k[0]*D/k[2])
