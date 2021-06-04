st= "010010"
l=[]
list1=[]
n=len(st)
for i in range(0,n-3):
    for j in range(i+1,n-2):
        for k in range(j+1,n-1):
            for m in range(k+1,n):
                    string=st[0:j]+'.'+st[j:k]+'.'+st[k:m]+'.'+st[m:]
                    l.append(string)
l=list(set(l))
#print(l)

for i in range(len(l)):
    temp=l[i].split('.')
    #print(temp)
    #print(temp[0])
    for j in range(0,4):
        if ((temp[j]=='0' )or (temp[j][0]!='0')) and (int(temp[j])>=0 and int(temp[j])<=255):
               f=1
        else:
            f=0
            break

    if f==1:
        list1.append(l[i])
print(list1)

