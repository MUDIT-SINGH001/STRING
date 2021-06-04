st="011011010"
count=0

l=[st[0]]

for i in range(1,len(st)):
   
    if l!=[]:
        if st[i]==l[-1]:
            l.pop()
            count+=1
            
        else:
            l.append(st[i])
    else:
        l.append(st[i])
print(count)
