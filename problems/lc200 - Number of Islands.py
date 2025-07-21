

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    islands = 0
    for y in range (0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "1":
                islands += 1
                grid = recursiveTouch(y, x, grid)
                # for r in grid: print(r)
                # print()
            else: continue

    # print(grid)
    return islands


def recursiveTouch(y, x, grid):
    # essentially we need check and see if each adjacent tile
    # is a land or water tile
    # since we traverse from top left to bottom right, it is sufficient to only
    # recursively call to tiles to the bottom and to the right and left
    # Make sure to check the edge cases

    top = 0
    bottom = len(grid)
    left = 0
    right = len(grid[0])

    # for r in grid: print(r)
    # print()
    if (y >= bottom) or (y < top) or (x < left) or (x >= right):
        # print("break", y, x)
        return grid

    # print("recurse", y, x)
    try:
        if grid[y][x] == "1":
            grid[y][x] = "0"
            recursiveTouch(y, x + 1, grid) # Right
            recursiveTouch(y, x - 1, grid) # Left
            recursiveTouch(y + 1, x, grid) # Down
            recursiveTouch(y - 1, x, grid) # Up
    except IndexError: pass
    return grid


def count_islands(mat):
    if len(mat) == 0:
        return 0
    n, m = len(mat), len(mat[0])
    islands = 0
    for i in range(n):
        for j in range(m):
            explore_island(mat, i, j)
            islands += 1
    return islands


def explore_island(mat, i, j):
    # base case
    if not (0 <= i < len(mat)) or not (0 <= j < len(mat[0])) or mat[i][j] != 1:
        return
    else:
        mat[i][j] = -1

    explore_island(mat, i + 1, j)
    explore_island(mat, i - 1, j)
    explore_island(mat, i, j + 1)
    explore_island(mat, i, j - 1)

test1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

test2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

test3 = [
    ["1","0","1","1","0","1","1"]
]

test4 = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]

test5 = [
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]
]

print(numIslands(test1)) # 1
print(numIslands(test2)) # 3
print(numIslands(test3)) # 3
print(numIslands(test4)) # 1
print(numIslands(test5)) # 4


