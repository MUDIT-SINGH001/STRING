import math
exp="{{{"
cl=exp.count('}')
op=exp.count('{')

d={'{':'}'}
l=[]

if len(exp)%2!=0:
    print(-1)
else:
    for i in range(len(exp)):
        if exp[i] =='{':
            l.append(exp[i])
            #print(l)
        
        elif (exp[i] =='}'):
            if l!=[]:
                pop=l.pop()
               # print(pop)
                if d[pop]==exp[i]:
                    cl-=1
                    op-=1
   # print(op,cl)
    rev=math.ceil(cl/2)+math.ceil(op/2)
    print(rev)
