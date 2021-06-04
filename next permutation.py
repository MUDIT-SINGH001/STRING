from itertools import permutations
arr=[3,2,1]
s=""
l1=[]

for i in range(len(arr)):
    s+=str(arr[i])
    
l=[i for i in (''.join(p) for p in permutations(s))if i>s]

l.sort()
if l==[]:
    arr.sort()
    print(arr)
else:
    print(l[0])
