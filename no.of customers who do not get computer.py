n=3
string="GACCBDDBAGEE"
temp,lis=[],[]
for i in range(len(string)):
    if len(lis)<n :
        lis.append(string[i])
    elif string[i] in lis:
        lis.remove(string[i])
    else:
        temp.append(string[i])
print(len(list(set(temp))))
        
