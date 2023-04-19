a = [2, 4, 6, 3, 7, 10]


for i in range(len(a)):
    #  initializing max_value_index with i so that we can update the max_value_index later
    max_val_index = i
    # starting second index to iterate though
    for j in range(i + 1, len(a)):
        # updating max_value_index if the current value is smaller than the previous one
        if a[j] < a[max_val_index]:
            # updating index j to update max_value_index
            max_val_index = j
    a[i], a[max_val_index] = a[max_val_index], a[i]

print(a)
