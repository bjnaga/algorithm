# binary search function to accept an array of integers and sorting them according order
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


flag = binary_search(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 'i')
if flag != -1:
    print('Found at index: ', flag+1)
else:
    print(
        "element is not found in array ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']")
