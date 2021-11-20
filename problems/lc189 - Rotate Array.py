





def rotate(A: [int], k):

    # reversing array technique?
    A = list(reversed(A))
    A[:k] = list(reversed(A[:k]))
    A[k:] = list(reversed(A[k:]))

    return A


a = [1,2,3,4,5,6,7]
print(rotate(a, 4))
# end goal of [4,5,6,7,1,2,3]







