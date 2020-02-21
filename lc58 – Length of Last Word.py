


def len_of_last_word(s: str) -> int:
    """
    Given a string s, find the length of the last "word" / substring with no spaces. essentially:
    s = s.split(" ")
    l = len(s)
    last_word = len(s[l - 1])
    """

    l = 0
    encountered_chars = False
    for i in reversed(range(len(s))):
        if s[i] == " " and not encountered_chars:
            continue
        elif s[i] != " ":
            encountered_chars = True
            l += 1
        else:
            return l
    return l




