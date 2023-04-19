lst = [1, 3, 5, 6, 8, 9, 10, 11, 12]
f = 0
for i in range(len(lst)):
    search = 7
    if search == lst[i]:
        print(lst[i], " Element found in the position", (i+1))
        f = 1
        break

if (f == 0):
    print("Element not found in the list")
