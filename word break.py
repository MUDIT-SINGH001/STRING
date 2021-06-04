B = [ "i", "like", "sam", "sung", "samsung", "mobile",
"ice", "icecream","go" ,"man","mango" ]
B.sort()
print(B)
A="maniceicecreamicream"

i=0
str=""
str2=""
substr=""
while i<len(A):
    
    for j in range(i+1,len(A)+1):
                if A[i:j] in B:
                    str=""
                    str+=A[i:j]
                    print(str)
                    if str  in B:
                        str2=""
                        str2+=str
                        print(str2,i)
                
                    
    print(str2)
    substr+=str2
    if substr=="":      
        i=i+1
    else:
        i=len(substr)
if substr==A:
    print(1)
else:
    print(0)

                        
                        
                                
                
                

