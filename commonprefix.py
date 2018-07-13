n=int(input())
l=[]
for i in range(n):
    v=raw_input()
    l.append(v)
str1=l[0]
str2=l[1]
if(len(str1)>len(str2)):
   maxlen=len(str2)
else:
   maxlen=len(str1)
result=""
for i in range(0,maxlen):
   if(str1[i]!=str2[i]):
       break
   else:
       result=result+str1[i]
print(result)
   
   
