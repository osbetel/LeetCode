

def intToRoman(n: int) -> str:
    """
    Given an integer n, convert it into roman numerals and return the string
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    """
    # approach? Try to subtract largest values first
    # ie: 1392. -1000 = M, 392, -300 = MCCC, 92, -90 = MCCCXC, 2, -2 = MCCCXCII
    # note that we can have 3 of the same character in a row, III, but not more.
    # 3 = III, 4 = IV which is 5 - 1 = 4

    # if it's negative, remember this (note the problem says integer, not positive integer so we need to account for this)
    negative = False
    if n < 0:
        negative = True
        n *= -1

    roman = ""
    d = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL',
    50:'L', 90:'XC',100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    for val in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
        # we can have as many M's / 1000's as we need, then subtract 900 CM, then 500 D, then 400 CD, etc.
        while (n - val) >= 0:
            n -= val
            roman += d.get(val)

    if negative: return "-" + roman
    return roman

# for a future modification, the romans would write a bar above a number to indicate multiplying by 1000,
# eg: Xbar = 10 * 1000 = 10000, instead of having to write M ten times
# Mbar would be 1 million, Dbar is 500k, Cbar is 100k, Lbar is 50k, Xbar is 10k. Vbar and Ibar are not necessary
# because we write 5000 as MMMMM and 1000 as M. (although you can use Vbar for conciseness I guess?)

# MCCCXCII
k = intToRoman(1392)
print(k)





