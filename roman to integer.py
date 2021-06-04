d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'0':0}
s=input()
s+="0"
i=0
su=0
while i<len(s)-1:
    #print(s[i])
    if d[s[i]]>=d[s[i+1]]:
        su+=d[s[i]]
        i+=1
    else:
        su+=d[s[i+1]]-d[s[i]]
     #   print(su)
        i+=2
       # print(i)
print(su)       
    
    
