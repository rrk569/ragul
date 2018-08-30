num=int(input())
ra=raw_input().split()
list1=[]
for i in ra:
    list1.append(int(i))
list1.sort()
for j in list1:
    print(j),
