


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def mergeSort(alist):

   # print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   # print("Merging ",alist)
   return alist




a = [1,2,45,5,1,2,6,76,12,3,6,6,1,3,6,6,87,98,9,9,98,12,3,7,6,32,2,764,745,8,89,2,34,
     1,23,5,6,2,85,4,63,9,5,1,78,4,251,1,5,4,65,6,4,321,68,498,498,4132,198,462,198,
     1,23,1685,42,1,496,4,4,84,4,44,4,4,4,4,4,4,4,4,4,45,84,651,78,42,168,4968,3,1,6]
# print(quicksort(a, 0, len(a) - 1))
print(mergeSort(a))



