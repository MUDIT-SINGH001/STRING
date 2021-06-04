
a =[
           [ 'e','e','a','a','c','d','a','b','e','d'],
            ['d','c','d','a','d','d','d','a','d','a'],
            ['e','e','d','e','c','a','b','e','c','e'],
            ['a','e','e','d','d','d','a','a','d','a'],
            ['b','c','b','a','d','c','c','c','e','b'],
            ['d','e','d','e','e','a','b','d','c','d']
      
           
           ]

str= "dcd"
length=len(str)-1
n=6
m=10

string=""
li=[]
if str!=str[::-1]:
    for i in range(n):                                                          #left/right
        for  j in range(m):
            if str[0] ==a[i][j] or str[-1]==a[i][j]:
                    string=""
                    k=j
                    while k<m:
        
                            string+=a[i][k]
                            k+=1
                            if string ==str :
                                li.append(list(map(int,(i,j))))
                                break
                            elif str[::-1]==string:
                                li.append(list(map(int,(i,k-1))))
                                break
else:
    for i in range(n):                                                          #left/right
        for  j in range(m):
            if str[0] ==a[i][j] or str[-1]==a[i][j]:
                    string=""
                    k=j
                    while k<m:
        
                            string+=a[i][k]
                            k+=1
                            if string ==str :
                                li.append(list(map(int,(i,j))))
                                li.append(list(map(int,(i,k-1))))
                                break
                           
    
        

if str!=str[::-1]:        
    for i in range(n):                  #up/down
        for j in range(m):
            
            if str[0] ==a[i][j] or str[-1]==a[i][j]:
                  #  print(a[i][j])
                    string=""
                    k=i
                    while k<n:
                            string+=a[k][j]
                            k+=1
                            if string ==str :
                                li.append(list(map(int,(i,j))))
                                break
                            elif str[::-1]==string:
                                li.append(list(map(int,(k-1,j))))
                                break
else:
    for i in range(n):                  #up/down
        for j in range(m):
            
            if str[0] ==a[i][j] or str[-1]==a[i][j]:
                  #  print(a[i][j])
                    string=""
                    k=i
                    while k<n:
                            string+=a[k][j]
                            k+=1
                            if string ==str :
                                li.append(list(map(int,(i,j))))
                                li.append(list(map(int,(k-1,j))))
                                break
                           
if str!=str[::-1]:  
    for  i in range(n):         #diagonal left
        for j in range(m):
             if str[0] ==a[i][j] or str[-1]==a[i][j]:
                    string=""
                    k=i
                    temp=j
                    while k<n and j>=0:
                        string+=a[k][j]
                        k+=1
                        j-=1
                        if string ==str :
                                li.append(list(map(int,(i,temp))))
                                break
                        elif str[::-1]==string:
                                li.append(list(map(int,(k-1,j+1))))
                                break
else:
    for  i in range(n):         #diagonal left
      for j in range(m):
         if str[0] ==a[i][j] or str[-1]==a[i][j]:
                string=""
                k=i
                temp=j
                while k<n and j>=0:
                    string+=a[k][j]
                    k+=1
                    j-=1
                    if string ==str :
                            li.append(list(map(int,(i,temp))))
                            li.append(list(map(int,(k-1,j+1))))
                            break
                   
                    
if str!=str[::-1]:
    for  i in range(n):         #diagonal right
        for j in range(m):
             if str[0] ==a[i][j] or str[-1]==a[i][j]:
                    string=""
                    k=i
                    temp=j
                    while k<n and j<m:
                        string+=a[k][j]
                    
                        j+=1
                        k+=1
                        if string ==str :
                                li.append(list(map(int,(i,temp))))
                                break
                        elif str[::-1]==string:
                                li.append(list(map(int,(k-1,j-1))))
                                break
else:
    for  i in range(n):         #diagonal right
        for j in range(m):
             if str[0] ==a[i][j] or str[-1]==a[i][j]:
                    string=""
                    k=i
                    temp=j
                    while k<n and j<m:
                        string+=a[k][j]
                    
                        j+=1
                        k+=1
                        if string ==str :
                                li.append(list(map(int,(i,temp))))
                                li.append(list(map(int,(k-1,j-1))))
                                break
                      
res = list(set(map(lambda i: tuple(i), li)))
res.sort()
print(res)
        
       
