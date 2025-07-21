# LeetCode Medium Problem Templates
# Study these patterns for common problem types

# ================================
# 1. TWO POINTERS
# ================================
def two_pointers_template(arr, target):
    """
    Use when: Array is sorted, looking for pairs/triplets, removing duplicates
    Examples: 3Sum, Container With Most Water, Remove Duplicates
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]  # Found pair
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # No pair found

# ================================
# 2. SLIDING WINDOW
# ================================
def sliding_window_template(s, k):
    """
    Use when: Subarray/substring problems with size constraints
    Examples: Longest Substring Without Repeating Characters, Max Sum Subarray
    Time: O(n), Space: O(k) for character set
    """
    left = 0
    char_count = {}
    max_length = 0
    
    for right in range(len(s)):
        # Expand window: add right character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Contract window if condition violated
        while len(char_count) > k:  # More than k unique chars
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length

# ================================
# 3. BINARY SEARCH
# ================================
def binary_search_template(arr, target):
    """
    Use when: Sorted array, finding target/insertion point, search space reduction
    Examples: Search Insert Position, Find Peak Element, Search in Rotated Array
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid  # Found target
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return left  # Insertion point if not found

# ================================
# 4. DYNAMIC PROGRAMMING (1D)
# ================================
def dp_1d_template(arr):
    """
    Use when: Optimal substructure, overlapping subproblems in sequence
    Examples: House Robber, Climbing Stairs, Maximum Subarray
    Time: O(n), Space: O(n) or O(1) with optimization
    """
    if not arr:
        return 0
    
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    
    for i in range(1, n):
        # Recurrence relation: current = max(take current + prev-prev, skip current)
        dp[i] = max(arr[i] + (dp[i-2] if i >= 2 else 0), dp[i-1])
    
    return dp[n-1]

# ================================
# 5. DYNAMIC PROGRAMMING (2D)
# ================================
def dp_2d_template(grid):
    """
    Use when: 2D grid problems, edit distance, longest common subsequence
    Examples: Unique Paths, Edit Distance, Coin Change 2D
    Time: O(m*n), Space: O(m*n)
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Base cases
    dp[0][0] = grid[0][0]
    
    # Fill first row and column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill rest of table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# ================================
# 6. BACKTRACKING
# ================================
def backtracking_template(candidates, target):
    """
    Use when: Generate all combinations/permutations, constraint satisfaction
    Examples: Subsets, Permutations, N-Queens, Word Search
    Time: O(2^n) or worse, Space: O(n) recursion depth
    """
    result = []
    
    def backtrack(current_combination, remaining_target, start_index):
        # Base case: found valid solution
        if remaining_target == 0:
            result.append(current_combination[:])  # Make copy
            return
        
        # Base case: invalid path
        if remaining_target < 0:
            return
        
        # Try all possible choices
        for i in range(start_index, len(candidates)):
            # Make choice
            current_combination.append(candidates[i])
            
            # Recurse with updated state
            backtrack(current_combination, remaining_target - candidates[i], i)
            
            # Backtrack: undo choice
            current_combination.pop()
    
    backtrack([], target, 0)
    return result

# ================================
# 7. BFS (LEVEL ORDER)
# ================================
from collections import deque

def bfs_template(root):
    """
    Use when: Shortest path, level-order traversal, minimum steps
    Examples: Binary Tree Level Order, Word Ladder, Rotting Oranges
    Time: O(V + E), Space: O(V)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes in current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # Add children to queue for next level
            if hasattr(node, 'left') and node.left:
                queue.append(node.left)
            if hasattr(node, 'right') and node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# ================================
# 8. DFS (RECURSIVE)
# ================================
def dfs_template(root):
    """
    Use when: Tree/graph traversal, finding paths, connected components
    Examples: Binary Tree Paths, Number of Islands, Course Schedule
    Time: O(V + E), Space: O(H) where H is height
    """
    if not root:
        return 0
    
    # Process current node
    result = root.val if hasattr(root, 'val') else 0
    
    # Recurse on children
    left_result = dfs_template(root.left) if hasattr(root, 'left') and root.left else 0
    right_result = dfs_template(root.right) if hasattr(root, 'right') and root.right else 0
    
    # Combine results
    return result + left_result + right_result

# ================================
# 9. UNION-FIND (DISJOINT SET)
# ================================
class UnionFind:
    """
    Use when: Dynamic connectivity, cycle detection, grouping elements
    Examples: Number of Connected Components, Redundant Connection
    Time: O(±(n)) per operation (nearly constant), Space: O(n)
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x == root_y:
            return False  # Already connected
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.components -= 1
        return True

# ================================
# 10. MONOTONIC STACK
# ================================
def monotonic_stack_template(arr):
    """
    Use when: Next/previous greater/smaller element, histogram problems
    Examples: Daily Temperatures, Largest Rectangle in Histogram
    Time: O(n), Space: O(n)
    """
    result = [0] * len(arr)
    stack = []  # Store indices
    
    for i in range(len(arr)):
        # Maintain decreasing stack (for next greater element)
        while stack and arr[stack[-1]] < arr[i]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index  # Distance to next greater
        
        stack.append(i)
    
    return result

# ================================
# 11. TRIE (PREFIX TREE)
# ================================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class Trie:
    """
    Use when: Prefix matching, word search, autocomplete
    Examples: Implement Trie, Word Search II, Design Add and Search
    Time: O(m) per operation where m is word length, Space: O(ALPHABET_SIZE * N * M)
    """
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# ================================
# 12. TOPOLOGICAL SORT
# ================================
def topological_sort_template(graph):
    """
    Use when: Dependency resolution, course scheduling, build order
    Examples: Course Schedule, Alien Dictionary
    Time: O(V + E), Space: O(V)
    """
    from collections import defaultdict, deque
    
    # Calculate in-degrees
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Start with nodes having no dependencies
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Remove this node and update in-degrees
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycle
    return result if len(result) == len(graph) else []