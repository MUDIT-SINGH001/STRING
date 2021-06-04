def rev(string):
    if string==string[::-1]:
        return True
    else:
        return False
def check(st,c):
    if not rev(st):
        c+=1
        lis=list(st)
        lis.pop()
        string=''.join(map(str,lis))
        check(string,c)
    else:
        print(c)
if __name__ == "__main__":
 
    st= "ABA"
    c=0
    check(st,c)
    
    
        
