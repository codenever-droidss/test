n = str(input())
max1 = 1
save = 1
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        save += 1
    else:
        if save > max1:
            max1 = save
        save = 1
if save > max1:
    max1 = save
print(max1)
