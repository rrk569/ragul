num=raw_input().split()
num1=int(num[0])
num2=int(num[1])
for i in range(num1+1,num2):
    n=i
    s=0
    while(n!=0):
        re=(n%10)
        re=re**3
        s=s+re
        n=n//10
    if(s==i):
        print(i),

    

    
