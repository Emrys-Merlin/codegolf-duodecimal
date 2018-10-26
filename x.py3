x=float(input())
r='-' if x<0 else ''
x=abs(x)
if x<1:
 r+='0'
c=0
n=int(x)
while x-n:
 x*=12
 n=int(x)
 c-=1
t=''
while n:
 t=([str(i) for i in range(10)]+['a','b'])[n%12]+t
 n//=12
r+=t
print(r[:c]+'.'+r[c:] if c else r,end='')
