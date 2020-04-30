# Sorting

arr = [8, 3, 6, 1, 4, 7, 5, 2]

def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        #print(arr)

    return arr

print(bubbleSort(arr))

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        # min swap to front
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr

print(selectionSort(arr))

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while(j >= 0 and arr[j] > arr[j+1]):    
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
    
    return arr

print(insertionSort(arr))

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    left = arr[:round(len(arr)/2)]
    right = arr[round(len(arr)/2):]
    # print(left, right)
    left = mergeSort(left)
    right = mergeSort(right)

    
    return merge(left, right)

def merge(left, right):
    print(left, right)
    i = 0
    j = 0
    arr = []
    
    while(i < len(left) or j < len(right)):
        if i == len(left):
            arr.append(right[j])
            j += 1
        elif j == len(right):
            arr.append(left[i])
            i += 1

        elif i < len(left) and left[i] < right[j]:
            arr.append(left[i])
            i += 1
        elif j < len(right) and left[i] > right[j]:
            arr.append(right[j])
            j += 1
    print(arr)
    return arr

print(arr)
print(mergeSort(arr))


arr = [4, 6, 2, 1, 7, 3, 5]

def quickSort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr

    i = - 1
    j = 0
    while j <= len(arr) - 2:
        if arr[j] < arr[-1]:
            i += 1
            temp  = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j += 1
    i += 1
    # put pivot to index i
    temp = arr[-1]
    arr[-1] = arr[i]
    arr[i] = temp
    
    left = quickSort(arr[:i])
    right = quickSort(arr[i+1:])

    result = (left + [arr[i]] + right)

    return result
    
print(quickSort(arr))

    
