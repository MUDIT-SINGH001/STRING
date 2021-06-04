from itertools import permutations
s="aab"
fl=0
l=[''.join(i) for i in permutations(s)]
l.sort()
l=list(set(l))
#print(l)
for i in l:
    #print(i)
    temp=i
    f=0
    for i in range(len(temp)-1):
        if temp[i]!=temp[i+1]:
            f+=1
            if f==len(temp)-1:
                fl=1
                print(temp)
        else:
        
            break
if fl==0:
    print("")
    
     
    
