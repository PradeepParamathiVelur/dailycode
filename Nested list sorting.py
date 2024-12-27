
l1=['john',1,'prd',5,'roc',3,'med',7,'app',1,'kud',3]
length=int(len(l1)/2)
l2=[]
z=0
for x in range(0,length):
    l2.append([])
    for y in range(0,2):
        l2[x].append(l1[z])
        z=z+1
for x in range (0,len(l2)):
    for y in range(x,len(l2)):
        if(l2[x][1]>l2[y][1]):
            a=l2[x]
            l2[x]=l2[y]
            l2[y]=a
l3=[l2[0][0]]
count=0
for x in range(0,len(l2)):
    if count==(len(l2)-1):
        break
    if(l2[x][1]>=l2[x+1][1]):
        l3.append(l2[x+1][0])
        count+=1
    else:
        break
for x in range (0,len(l3)):
    for y in range(x,len(l3)):
        if(l3[x]>l3[y]):
            a=l3[x]
            l3[x]=l3[y]
            l3[y]=a
for x in range(0,len(l3)):
    print(l3[x])










