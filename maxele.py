a=[1,2,4,6,7,5]
max =a[0]
for i in range(len(a)):
    if(max < a[i]):
        max = a[i]
print(max)