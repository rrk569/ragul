num=raw_input().split()
num1=int(num[0])
num2=int(num[1])
for num3 in range(num1+1,num2):
     if num3 > 1:
       for i in range(2,num3):
           if (num3 % i) == 0:
               break
       else:
           print(num3),
