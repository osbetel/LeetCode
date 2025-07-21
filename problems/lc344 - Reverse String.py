




def reverseString(s):
    # s is an array of characters
    # must be an in-place reversal
    l = len(s)
    left = 0
    right = l - 1
    for i in range(l // 2):
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1
    return s


s = []
print(reverseString(s))



