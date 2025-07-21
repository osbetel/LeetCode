


def reverseWords(s: str):
    sarr = s.split(" ")
    if len(sarr) == 1:
        return s[::-1]
    else:
        return " ".join([x[::-1] for x in sarr])


s = "the quick brown fox jumps over the lazy dog"
print(reverseWords(s))

