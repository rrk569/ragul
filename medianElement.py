num=int(input())
ra=raw_input().split()
list1=[]
for i in ra:
    list1.append(int(i))
list1.sort()
m=sum(list1)
n=m//num
print(n),
