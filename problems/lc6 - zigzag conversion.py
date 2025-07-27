"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""

def transpose_with_zip(matrix):
    return list(map(list, zip(*matrix))) if matrix else []


def convert(s, num_rows):
    # I'm certain this can be represented in a mathematical formula
    # PAYPALISHIRING, with num_rows = 3
    # PAHNAPLSIIGYIR

    # first generate a matrix of height = num_rows and width = len(s)
    # how do we determine width? A string can be thought of as a matrix of 1xL
    # at num_rows = 2, we would use a matrix of size 2x7
    # at num_rows = 3 we use a matrix of size 3x7
    # at num_rows = 4 we use matrix of size 4x7
    # def transpose_matrix(m):
    #     return list([x for x in zip(m)])
    # zigzag = [["-"] * (len(s)//2) for n in range(num_rows)]
    # first = 0
    # for i in range(len(s)):
    #     if i % num_rows == 0:
    #         pass
    pass

def convert(s, numRows):
    """
    Convert string from zigzag pattern to line-by-line reading
    
    Args:
        s: input string
        numRows: number of rows in zigzag pattern
    
    Returns:
        converted string read line by line
    """
    # Edge case: if only 1 row or string shorter than numRows
    if numRows == 1 or len(s) <= numRows:
        return s
    
    # Create list to store characters for each row
    rows = [''] * numRows
    
    # Track current row and direction
    current_row = 0
    going_down = False
    
    # Process each character
    for char in s:
        # Add character to current row
        rows[current_row] += char
        print(rows)
        
        # Change direction at top or bottom
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        
        # Move to next row
        current_row += 1 if going_down else -1
    
    # Join all rows to get final result
    return ''.join(rows)

# Test with the given examples
def test_solution():
    # Example 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    result1 = convert(s1, numRows1)
    print(f"Input: s = '{s1}', numRows = {numRows1}")
    print(f"Output: '{result1}'")
    print(f"Expected: 'PAHNAPLSIIGYIR'")
    print(f"Match: {result1 == 'PAHNAPLSIIGYIR'}")
    print()
    
    # Example 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    result2 = convert(s2, numRows2)
    print(f"Input: s = '{s2}', numRows = {numRows2}")
    print(f"Output: '{result2}'")
    print(f"Expected: 'PINALSIGYAHRPI'")
    print(f"Match: {result2 == 'PINALSIGYAHRPI'}")
    print()
    
    # Edge case
    s3 = "A"
    numRows3 = 1
    result3 = convert(s3, numRows3)
    print(f"Input: s = '{s3}', numRows = {numRows3}")
    print(f"Output: '{result3}'")
    print(f"Expected: 'A'")
    print(f"Match: {result3 == 'A'}")

# Run tests
test_solution()


a = "PAYPALISHIRING"
convert(a, 3)

# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# m2 = [reversed(x) for x in m]
# t = transpose_with_zip(m2)
# for r in t:
#     print(list(reversed(r)))