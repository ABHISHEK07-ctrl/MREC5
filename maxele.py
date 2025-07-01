a = [1, 2, 6, 7, 3, 4]
first = second = float('-inf')
for num in a:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)
