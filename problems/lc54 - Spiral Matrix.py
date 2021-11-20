# Given a matrix of m x n elements (m rows, n columns),
# return all elements of the matrix in spiral order.
#
# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix: [[int]]):
    def spiralCoordinates(y1, x1, y2, x2):
        for x in range(x1, x2 + 1):
            yield y1, x
        for y in range(y1 + 1, y2 + 1):
            yield y, x2
        if y1 < y2 and x1 < x2:
            for x in range(x2 - 1, x1, -1):
                yield y2, x
            for y in range(y2, y1, -1):
                yield y, x1

    if not matrix: return []
    res = []
    y1, y2 = 0, len(matrix) - 1
    x1, x2 = 0, len(matrix[0]) - 1

    while y1 <= y2 and x1 <= x2:
        for y, x in spiralCoordinates(y1, x1, y2, x2):
            res.append(matrix[y][x])
        y1 += 1
        y2 -= 1
        x1 += 1
        x2 -= 1


    return res

def spiralOrder2(matrix: [[int]]):
    res = []

    while len(matrix) > 0:
        res.extend(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1]
    return res

m = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
s = "aisjdoiajsodijasd"
print(*m[0])
# * refers to the contents of the object
# kind of like a pointer, but to an object's internals
# so if a = [1,21,3,4] then *a = 1 21 3 4

