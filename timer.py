def timer(fx, *args):
    import time
    start = time.clock()
    fxr = fx(*args)
    print("function return: " + str(fxr))
    end = time.clock()
    print("execution time (s): " + str(end - start))
    return fxr