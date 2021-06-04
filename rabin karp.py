str="abcddcabefgaabcdcd"
p="cdcd"
n=len(str)
m=len(p)
asc=0
asc2=0
for i in range(m):
    asc+=ord(p[i])
asc=asc%1500
for i in range(0,n-m+1):
    str1=str[i:i+m]
    for j in range(m):
        asc2+=ord(str1[j])
        #print(asc)
    asc2=asc2%1500
    if asc2==asc and str1==p:
        print(i)
    else:
        asc2=0
        
        
        
        
    

