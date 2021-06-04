s="abaabab"

l=[]
p=0
l.append(s[0])
for i in range(1,len(s)):
    if l[p]!=s[i]:
        l.append(s[i])
        p+=1
        
    
print("".join(l))
