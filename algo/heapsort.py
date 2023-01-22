# heapsort


def heapify(arr, arrlen, root):
    largest = root
    l = 2*root+1
    r = 2*root+2

    if l < arrlen and arr[root] < arr[l]:
        largest = l
    if r < arrlen and arr[largest] < arr[r]:
        largest = r
    if largest != root:
        (arr[root], arr[largest]) = (arr[largest], arr[root])
        heapify(arr, arrlen, largest)
    print(arr)

def getMaxFromHeap(arr):
    sortedArray = []
    for i in range(len(arr)-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
    return arr


def heapsort(arr):

    l = len(arr)

    # children of heaps will be for idx k will be 2k+1, 2k+2
    # for array of len l = 2k+2, last parent will be at l//2-1
    # start build heap from bottom up last parent
    for i in range(l//2-1, -1, -1):
        heapify(arr, l, i)
    return arr

arr = heapsort([234,456,474,245,5,547,756,6523])
print(getMaxFromHeap(arr))