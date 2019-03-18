

# only functions on a sorted list
def binarySearch(alist, item):
        first = 0
        last = len(alist)-1
        found = False

        while first <= last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1

        return found

a = [1,2,45,5,1,2,6,76,12,3,6,6,1,3,6,6,87,98,9,9,98,12,3,7,6,32,2,764,745,8,89,2,34,
     1,23,5,6,2,85,4,63,9,5,1,78,4,251,1,5,4,65,6,4,321,68,498,498,4132,198,462,198,
     1,23,1685,42,1,496,4,4,84,4,44,4,4,4,4,4,4,4,4,4,45,84,651,78,42,168,4968,3,1,6]
a.sort()
print(binarySearch(a, 9))







