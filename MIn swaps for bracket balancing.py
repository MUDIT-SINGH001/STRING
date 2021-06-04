
def checkbalance(exp,sw):
    
    for i in range(len(exp)):
        if exp[i]==']':
            op=exp[0:i+1].count('[')
            cl=exp[0:i+1].count(']')
            if op <cl:
                j=exp[i+1:].index('[')
                
                checkbalance(swap(i,j,exp,sw))
    print(sw)          
                
                
def swap(i,j,exp,sw):
    temp =exp[j-1]
    exp[j-1]=exp[j]
    exp[j]=temp
    sw+=1
    return sw
    return (exp)
    



if __name__ == "__main__": 
    ex= "[][]][]["
    exp=list(ex)
    sw=0
    checkbalance(exp,sw)
    
