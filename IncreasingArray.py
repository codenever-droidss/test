n = int(input())
t = list(map(int, input().split()))
dem = 0

for i in range(1, n):
    if t[i] < t[i - 1]:
        dem += t[i - 1] - t[i]
        t[i] = t[i - 1]
print(t)
print(dem)
