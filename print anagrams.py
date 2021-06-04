from itertools import permutations
def permut(string):
    list1=[''.join(p) for p in permutations(string)]
    return list1

def check(lis,strs,nl):
    list2=[]
    i=0
    while i<len(strs):
        
        if strs[i] in lis:
             list2.append(strs[i])
             strs.remove(strs[i])
        else:
            i+=1
             
    nl.append(list2)
    return (strs,nl)
     
   
if __name__ == "__main__":
  strs = ["act","god","cat","dog","tac"]
  
  nl=[]
  while strs!=[]:
      lis=permut(strs[0])
      strs,nl=check(lis,strs,nl)
      nl=nl[::-1]
  print(nl)
      
  
     
     
