str1="pijp"


str2="akka"
f1=0
f2=0
lis=set(list(zip(str1,str2)))

print(lis)
len1=len(set(str1))
print(set(str1))
len2=len(lis)
if len1==len2:
    f1=1
else:
    f1=0
lis=set(list(zip(str2,str1)))


len1=len(set(str2))

len2=len(lis)
if len1==len2:
    f2=1
else:
    f2=0
if f1==1 and f2==1:
    print(1)
else:
    print(0)
    
