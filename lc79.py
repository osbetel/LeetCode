# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


def wordFind(board: [[str]], word):
    # for each instance of the first letter in the word, see if the following
    # letter is adjacent to the current one
    # Best to make this a recursive function


    for i in range(0, len(board)):
        for j in range(0, len(board[i])):

            if checkAdjacents(board, word, i, j, 0): return True

    return False

def checkAdjacents(board: [[str]], word, i, j, k):
    if k == len(word): return True
    if i < 0 or j < 0 or i == len(board) or j == len(board[i]): return False
    if board[i][j] != word[k]: return False

    board[i][j] += "-"
    exist = (
            checkAdjacents(board, word, i + 1, j, k + 1) or
            checkAdjacents(board, word, i - 1, j, k + 1) or
            checkAdjacents(board, word, i, j + 1, k + 1) or
            checkAdjacents(board, word, i, j - 1, k + 1)
    )
    board[i][j] = board[i][j].strip("-")
    return exist



print(wordFind([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False
print(wordFind([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(wordFind([["a","a"]], "aaa")) # False
print(wordFind([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")) # True





