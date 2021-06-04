from collections import Counter
st="ADOBECODEBANC"

pt="ABC"

c=len(pt)                                                              
minlen=float("inf")
d=Counter(pt)
items=d.keys()
i,j=0,0
while j<len(st):
       while j<len(st) and c!=0:
               if st[j] in items:
                       d[st[j]]-=1
                       if d[st[j]]==0:
                           c-=1
               else:
                    j=j+1    
       while i<j and c==0: 
                      
                       if j-i<minlen:
                            minlen=j-i
                            temp=st[i:j]
                       if st[i] in items:
                                d[st[i]]+=1
                                if d[st[i]] >0:
                                    c+=1
                       i+=1
        
                
                            
print(temp)            



