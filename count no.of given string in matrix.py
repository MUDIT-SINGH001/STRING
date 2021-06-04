
a =[
            ['D','D','S','G','D','D'],
            ['B','G','K','E','K','S'],
            ['S','K','E','E','G','K'],
            ['D','D','E','D','D','E'],
            ['D','D','G','D','D','E'],
            ['D','D','D','D','D','G']
           ]
str= "GEEKS"
c=0
string=""
for i in range(len(a[0])):
    temp="".join(a[i])
    if str in temp or str[::-1] in temp:
        c+=1
print(c)
for i in range(len(a[0])):
    for j in range(len(a[0])):
        
        if str[0] ==a[i][j] or str[-1]==a[i][j]:
                print(a[i][j])
                string=""
                k=i
                while k<len(a[0]):
                        string+=a[k][j]
                        k+=1
                        if string ==str or str[::-1]==string:
                            c+=1
                            break
print(c)
                
        

        
       
