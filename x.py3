r=''
for i,s in enumerate(input().split('.')):
 e=-(-1)**i
 n=float('.'*i+s)*12**i
 r+='.'*i
 while n:
  m=int(n)
  r+=f'{m%12:x}'
  n=(n-m*i)*12**e
  n=[int(n),n][i]
 r=(r+'0'*(1-len(r))+'-'*('-'in s))[::e]
print(r)
