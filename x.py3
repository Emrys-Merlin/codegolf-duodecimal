y=float(input())
x=abs(y)
r=''
c=1
n=int(x)
while x-n:
 x*=12
 n=int(x)
 c-=1
while n:
 c+=1
 r='.'*(c==1)+f'{n%12:x}'+r
 n//=12
print('-'*(y<0)+'0'*(c==1)+r)
