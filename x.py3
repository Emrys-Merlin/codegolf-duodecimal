y=float(input())
r=''
x=abs(y)
if x<1:
 r+='0'
c=1
n=int(x)
while x-n:
 x*=12
 n=int(x)
 c-=1
while n:
 r+=([str(i) for i in range(10)]+['a','b'])[n%12]+('' if c else '.')
 n//=12
 c+=1
if y<0:
 r+='-'
print(r[::-1],end='')
