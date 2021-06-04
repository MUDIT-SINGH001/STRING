str1 = "onehello"
str2 = "hellofourtwooneworld"
str1=sorted(str1)
##print(str1)
if len(str1)<len(str2):
    for i in range(len(str1)):
        temp=str2[i:i+len(str1)]
        temp=sorted(temp)
       # print(temp)
        if(str1==temp):
            print("YES")
            break
        
