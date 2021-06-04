s=input()
c=0
res = [s[i: j] for i in range(len(s))for j in range(i + 1, len(s) + 1) ]
print(res)
for i in range(len(res)):
    if res[i]=="".join(list(map(str,reversed(res[i])))):
        c+=1
print(c)
