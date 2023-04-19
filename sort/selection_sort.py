a = [2, 4, 6, 3, 7, 10]


for i in range(len(a)):
    print(i)
    max_val_index = i
    for j in range(i + 1, len(a)):
        if a[j] < a[max_val_index]:
            max_val_index = j
    a[i], a[max_val_index] = a[max_val_index], a[i]

print(a)
