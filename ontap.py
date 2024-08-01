n = str(input())

max = 1
save = 1

for i in range(1,len(n)):
    if n[i] == n[i-1]:
        save+=1
    else:
        if save > max:
            max= save
        save=1
if save > max:
    max = save
print(max)