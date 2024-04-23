n=int(input())
a=[1]
count=2
for i in range(0,n+1):
    a.append(a[i]+count)
    count=2 if count==3 else 3
print(a[n-1])