""" Write a program to print the unique indices of all the numbers in the list which add up to target.
l = [1, 2, 33, 4, 5, 3, 99, 122, 6]
target = 7 For example,

# l = [1, 2, 33, 4, 43, 32, 99, 122, 7]
# target = 8 output: 0, 8 """


l = [1, 2, 33, 4, 5, 3, 99, 122, 6]
target = 7

pairs = []

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            pairs.append((i, j))

print("Unique index pairs that add up to target:")
for p in pairs:
    print(p)

# find second largest number

l = [20, 3, 90, 60]

l_sorted = sorted(l, reverse=True)
print("Second largest number:", l_sorted[1])

#approch-2
l = [20, 3, 90, 60]

largest = second = float('-inf')

for num in l:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number:", second)

#3rd approach
l = [20, 3, 90, 60]

print("Second largest number:", sorted(set(l))[-2])





