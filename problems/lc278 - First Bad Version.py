

def isBadVersion(v):
    pass

def firstBadVersion(n):
    # suppose there is a list of integers representing version,
    # [1...n] xome version x is bad and thus all subsequent versions are bad.
    # we have an API function isBadVersion(v) which returns ture/false. Minimize API calls
    # can use a binary search here. first bad version should come immediately after a good version
    # and be followed by a more bad versions, OR be the first element
    if n == 1:
        return 1
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        bv = isBadVersion(mid)
        if bv and left < mid:
            if not isBadVersion(mid - 1):
                return mid
        elif bv and left == mid:
            return mid

        if bv:  # if true, left subarray
            right = mid - 1
        else:
            left = mid + 1




