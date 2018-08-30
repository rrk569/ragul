num=int(input())
n=num
s=0
while(n!=0):
    re=(n%10)
    re=re**3
    s=s+re
    n=n//10
if(s==num):
    print("yes")
else:
    print("no")
    
    
