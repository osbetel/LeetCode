def solution(requestTimestamps, windowLength, maxInWindow):
    # requestTimestamps same source, chrono sorted
    # windowLength - size of window by timestamp, in seconds
    # maxInWindow - more requests than this in a timeframe get rate limited
    # requests = [ 1, 3, 4, 6 ]
    # windowLength = 4
    # maxInWindow = 2
    # [ true, true, false, true ]
    
    # brute force - iterate through requests count all in window check if outside of bounds,
    # if outside, mark that as false, otherwise true.
    
    res = []
    for i in range(len(requestTimestamps)):
        current_request = requestTimestamps[i]
        count = 0  # count how many valid requests in a window ending at some time T
        
        for j in range(i + 1):
            # check requests 
            check_request = requestTimestamps[j]
            if check_request >= (current_request - windowLength + 1):
                count += 1 # then counted valid
                
        # check for maxInWindow
        print(i, count, res)
        res.append(count <= maxInWindow)
            
    return res


def rateLimiter(requestTimestamps, windowLength, maxInWindow):
    result = []
    allowed_requests = []
    
    for timestamp in requestTimestamps:
        # Count allowed requests within current window
        count = 0
        for allowed_time in allowed_requests:
            if allowed_time >= timestamp - windowLength + 1:
                count += 1
        
        # Check if current request can be allowed
        if count < maxInWindow:
            result.append(True)
            allowed_requests.append(timestamp)
        else:
            result.append(False)
    
    return result
                
    
test_cases = [
    [[ 1, 3, 4, 6 ], 4, 2],
    [[ 1, 3, 5, 6 ], 4, 2]
]

expected = [
    [True, True, False, True],
    [True, True, True, False]
]

for t in test_cases:
    print(rateLimiter(*t))