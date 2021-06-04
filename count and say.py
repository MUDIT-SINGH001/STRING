n=int(input())

if n==1:
    print("1")
elif n==2:
    print("11")
else:
    lst="11"
    for i in range(3,n+1):
        
        c1=1
        temp=""
        for j in range(1,len(lst)):
                if lst[j]==lst[j-1]:
                    c1+=1
              
                else:
                    temp+=str(c1)+lst[j-1]
                    c1=1
                   # temp+=str(c1)+str(lst[j])
        temp+=str(c1)+lst[j]
        lst=temp
        
    print(lst)
        
