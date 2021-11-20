from functools import reduce
from operator import ior, iand


a = [
    [2,1,2],
    [2,1,2],
    [2,1,2]
]

def is_winning_board(b):
    checks = []
    # check horizontals
    for row in b:
        checks.append(reduce(iand, row))
    # check verticals
    for col in transpose(b):
        checks.append(reduce(iand, col))

    # check diagonals
    for d in diagonal(b):
        checks.append(reduce(iand, d))
    v = reduce(ior, checks)
    print(v)
    if v == 1:
        # X has a win on the board
        pass
    elif v == 2:
        # O has a win on the board
        pass
    elif v == 3:
        # if not 1 and not 2, then must be 3 indicating both players have a win state on the board
        pass
    return bool(v)

def transpose(m):
    return list(zip(*m))

def diagonal(m):
    return [
        [m[i][i] for i in range(len(m))],               # top left to bottom right
        [m[len(m) - i - 1][i] for i in range(len(m))]   # bottom left to top right
    ]


# 2, 0
# 1, 1
# 0, 2


print(is_winning_board(a))



