class Node:

    def __init__(self, value, neighbors):
        self.val = value
        self.neighbors = neighbors


class Graph:
    def __init__(self, nodes: [Node]):
        self.nodes = nodes

def longestPath(graph):
    l = 0
    for n in graph.nodes:
        # print(n.neighbors)
        if n.neighbors == []:
            return 1
        l = max(longestPathStartingAtNode(n, 0, []))
    return l


def longestPathStartingAtNode(node, length, visited):

    if node in visited and len(node.neighbors) == 1:
        return length

    else:
    # # does have neighbors
    # # n.neighbors exists
        mx = 0
        visited.append(node)
        for n in node.neighbors:
            # print(node.val)
            mx = max(mx, longestPathStartingAtNode(n, length + 1, visited))
            # print(longestPathStartingAtNode(n, length + 1, node))

    return mx

# A – C
# |
# B
# | \
# D   E
#     |
#     F



A = Node("A", [])
C = Node("C", [])
B = Node("B", [])
E = Node("E", [])
F = Node("F", [])
D = Node("D", [])
A.neighbors = [C, B]
B.neighbors = [D,E,A]
C.neighbors = [A]
D.neighbors = [B]
E.neighbors = [B,F]
F.neighbors = [E]





graph = Graph([A,B,C,D,E,F])

print(longestPath(graph))

