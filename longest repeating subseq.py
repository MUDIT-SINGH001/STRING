s= "pfoslsszfx"

res = [s[i: j] for i in range(len(s))for j in range(i + 1, len(s) + 1)]
maxi=1
res.sort(key=len,reverse=True)
print(res)

for i in range(len(res)):
    count=res.count(res[i])
    
    maxi=max(maxi,count)
    if maxi>1:
        print(len(res[i]))
        break
        
if maxi==1:
    print(0)
        
