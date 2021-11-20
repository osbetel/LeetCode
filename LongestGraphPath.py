class Node:

    def __init__(self, value, neighbors):
        self.val = value
        self.neighbors = neighbors

    def __str__(self):
        return self.val


class Graph:
    def __init__(self, nodes: [Node]):
        self.nodes = nodes


    def __str__(self):
        s = ""
        for n in self.nodes:
            s += f"{n} --> {[k.val for k in n.neighbors]}\n"
        return s

def longestPath(graph):
    paths = []
    for n in graph.nodes:
        paths.append(longestPathStartingAtNode(n, 0, []))
    return paths


def longestPathStartingAtNode(node, length, visited):
    print(node.val, length, [v.val for v in visited])
    if node in visited:
        return length
    else:
        mx = 0
        # haven't visited this node before
        visited.append(node)
        for n in node.neighbors:
            mx = max(length, longestPathStartingAtNode(n, length + 1, visited))
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
print(graph)

print(longestPath(graph))

