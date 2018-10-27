y=float(input())
r=''
x=abs(y)
t=r
if x<1:t='0'
c=1
n=int(x)
while x-n:
 x*=12
 n=int(x)
 c-=1
while n:
 r+=([f'{i:x}' for i in range(12)])[n%12]+('' if c else '.')
 n//=12
 c+=1
if y<0:t+='-'
print((r+t)[::-1],end='')
