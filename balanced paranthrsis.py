exp="{{}}[[{()}]]()"
D={'[':']','{':'}','(':')'}
l=[]
f=1
op=['[','{','(']
close=[']','}',')']
c=0
if len(exp)%2!=0:
    print("False")
else:
    for i in range(len(exp)):
        if exp[i] in op:
            l.append(exp[i])
           # print(l)
        
        elif (exp[i] in close):
            if l!=[]:
                pop=l.pop()
                if D[pop]==exp[i]:
                    c+=1
                
            else:
                f=0
                break
            
    if c==len(exp)/2:
        print ("YES")
    elif f==0:
        print("False")
    else:
        print("False")
