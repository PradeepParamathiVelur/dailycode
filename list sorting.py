
l1=[1,2,1,4,5,6,35,4]

for x in range (0,len(l1)):
    for y in range(x,len(l1)):
        if(l1[x]>l1[y]):
            a=l1[x]
            l1[x]=l1[y]
            l1[y]=a
print(l1)


