s1="EACAD"
s2="DACAE"
n=5
i=n-1
j=n-1
count=0
#while i>=0:
while j>=0 and i>=0:
        if s2[j]!=s1[i]:
            count+=1
            i-=1
        else:
            i-=1
            j-=1
print(count)
