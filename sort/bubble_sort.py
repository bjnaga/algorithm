a = [2, 4, 2, 6, 3, 7, 10]

# function to accept an array of numbers as list and sort them using bubble sort


def bubble_sort(a):
    for i in range(len(a)):
        swap = False
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        #         swap = True
        # if (swap == False):
        #     break
        # adding the above code will further optimize the bubble sort search


bubble_sort(a)
print(a)
