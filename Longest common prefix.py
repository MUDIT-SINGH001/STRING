strs=["abf","a"]
strs.sort()
flag=0
ans=""
if len(strs)==1:
    print(strs[0])
else:
    string=strs[0]

    for i in range(len(string),0,-1):
        f=0
        for j in range(1,len(strs)):
            if string[0:i]==strs[j][0:i]:
                f+=1
                if f==len(strs)-1:
                    flag=1
                    ans=string[0:i]
                    break
        if flag==1:
            break
    print(ans)
