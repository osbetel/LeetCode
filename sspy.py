def sellSpy():
    initialBal = 150
    valuePerContract = 5
    time = 52*3*10
    factor = 1.0
    import random


    # formula would be initialBal + numContracts * valuePerContract, each loop
    for i in range(1, time+1):
        if initialBal < 10000: factor = 1.0
        if initialBal >= 10000: factor = .70
        if initialBal >= 25000: factor = .28
        if initialBal >= 50000: factor = .14
        if initialBal >= 100000: factor = 0.07

        toAdd =  -(-initialBal*factor//50)*valuePerContract
        r = random.randint(1, 50)
        if r == 1:
            initialBal -= initialBal
            initialBal += toAdd
        else:
            initialBal += toAdd
        # print(i, r, round(initialBal,2))
    return initialBal


avg = 0
for x in range(5000):
    avg += sellSpy()
print(avg/5000)


