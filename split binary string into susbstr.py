str="1000110100"
countz=0
counto=0
subst=0
for i in range(len(str)):
     
     if str[i]=='0':
         countz+=1
        
     else:
         counto+=1
     if counto==countz:
            subst+=1
            #print(subst)
if counto!=countz:
    print(-1)
else:
    print(subst)
    
    
