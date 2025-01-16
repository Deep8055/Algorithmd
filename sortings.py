a = [4, 5, 2, 1, 8, 9, 7, 3, 12]
bubblearr = a
insertionarr = a
selectionarr = a
mergearr = a
quickarr = a
min = 100
max = 0
n = len(a)


##############################################################
# bubble sort
def bubblesort(bubblearr):
    for i in range(len(bubblearr)):
        for j in range(i + 1, len(bubblearr)):
            if bubblearr[i] > bubblearr[j]:
                temp = bubblearr[i]
                bubblearr[i] = bubblearr[j]
                bubblearr[j] = temp
    return bubblearr


# answer = bubblesort(bubblearr)
# print(answer)
####################################################################


#####################################################################
# merge sort
def mergesort(mergearr):
    if len(mergearr) > 1:
        mid = len(mergearr) // 2

        leftarr = mergearr[:mid]
        rightarr = mergearr[mid:]

        mergesort(leftarr)
        mergesort(rightarr)

        i = j = k = 0
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] <= rightarr[j]:
                mergearr[k] = leftarr[i]
                i = i + 1
            else:
                mergearr[k] = rightarr[j]
                j = j + 1
            k = k + 1

        while i < len(leftarr):
            mergearr[k] = leftarr[i]
            i = i + 1
            k = k + 1

        while j < len(rightarr):
            mergearr[k] = rightarr[j]
            j = j + 1
            k = k + 1


# mergesort(mergearr)
# print(mergearr)

################################################################################################
# quick sort


def partition(quickarr, low, high):
    pivot = quickarr[high]
    i = low - 1
    print("value of i:", i, "and value of quickarr[i]: ", quickarr[i])

    for j in range(low, high):
        if quickarr[j] <= pivot:
            i = i + 1
            (quickarr[i], quickarr[j]) = (quickarr[j], quickarr[i])

    (quickarr[i + 1], quickarr[high]) = (quickarr[high], quickarr[i + 1])

    return i + 1


def quicksort(quickarr, low, high):
    if low < high:
        pi = partition(quickarr, low, high)
        quicksort(quickarr, low, pi - 1)
        quicksort(quickarr, pi + 1, high)


# quicksort(quickarr, 0, len(quickarr)-1)
# print(quickarr)


################################################################################################
# insertion sort
def insertionsort(insertionarr):
    for i in range(1, len(insertionarr)):
        key = insertionarr[i]
        j = i - 1
        while j >= 0 and insertionarr[j] > key:
            insertionarr[j + 1] = insertionarr[j]
            j = j - 1
            insertionarr[j + 1] = key

    return insertionarr


answer = insertionsort(insertionarr)
print("insertion sort: ", answer)

a = [4,5,2,1,8,9,7,3]
n = len(a)

for i in range(n):
    key = a[i]
    j = i-1
    while j>=0 and a[j]>key:
        a[j+1] = a[j]
        a[j] = key
        j=j-1

# print(a)


################################################################################################
# insertion sort
def selectionsort(selectionarr):
    for i in range(len(selectionarr)):
        minid = i
        for j in range(i + 1, len(selectionarr)):
            if selectionarr[minid] > selectionarr[j]:
                minid = j
        selectionarr[i], selectionarr[minid] = selectionarr[minid], selectionarr[i]

    return selectionarr


# answer = selectionsort(selectionarr)
# print(answer)

################################################################################################
