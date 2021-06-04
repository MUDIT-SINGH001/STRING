st="CCCbAbbBbbC"
length=len(st)
f=0                                                                                 ##{'C', 'B', 'A', 'b'}
l=set(st)
lim=len(l)
while lim<=length:
    for i in range(0,length-lim+1):
        sub=st[i:i+lim]
        if (all(item in sub for item in l)):
            f=1
            break
    if f==1:
        print(lim)
        break
   
    lim+=1

