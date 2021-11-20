

def validNumber(n : str) -> bool:
    try:
        s = eval(n)
    except (NameError, SyntaxError) as err:
        if n == "e":
            return True
        return False
    if isinstance(s, int) or isinstance(s, float):
        # need to check --x and -+x, etc. cases
        # although I would consider them to be numbers...
        signs = ["-","+"]
        if len(n) >= 3:
            if n[0] and n[1] in signs:
                return False
        return True
    return False


l = ["a","b","e", "e.","2e-9","1.82e-5","17", "-12",
     "--2", "+-4", "-+3", "4--2"]
for x in l:
    r = validNumber(x)
    print(r)

