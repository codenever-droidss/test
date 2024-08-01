n=str(input())
m=1
f=1
for i in range(1,len(n)):
    if n[i] == n[i-1]:
        f+=1
    else:
        if f > m:
            m = f
        f=1
if f > m:
    m=f
print(m)
