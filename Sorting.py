


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


def mergesort2(lst):
    # print(lst)
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = mergesort2(lst[:mid])
    right = mergesort2(lst[mid:])

    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    # one of the two halves is empty
    # print(left[i:], right[j:], res)
    res.extend(left[i:])
    res.extend(right[j:])
    # print(res)
    # print()
    return res




import random
import time

a = [random.randint(0, 1000) for x in range(50000)]

start = time.time()
k = quicksort(a, 0, len(a) - 1)
# k = mergeSort(a)
# k = mergesort2(a)
# print(k)
print(time.time() - start)
assert k == sorted(a)
n, m, o = [4,4,4]
mat = [[[0] * o] * m] * n
from pprint import pprint
pprint(mat)



