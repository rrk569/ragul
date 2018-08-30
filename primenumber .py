import math
num=input()
r=0
for i in range(2,int(math.sqrt(num)+1)):
    if(num%i==0):
        r=1
if(r==1):
    print("no")
else:
    print("yes")
    
