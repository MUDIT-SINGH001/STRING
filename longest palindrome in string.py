s = "ayaxzfbjbkrxiri"
res = [s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)]
l=[]
for i in range(len(res)):
    
    
    if res[i]==(res[i][::-1]):
        
        l.append(res[i])
l.sort(key=len)
print(l)
m=len(l[-1])
if m>1:
    for i in range(len(l)):
        if len(l[i])==m:
            print (l[i])
            break
else:
    print (l[0])
    
