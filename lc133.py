# Given the head of a graph, return a deep copy (clone) of the graph.
# Each node in the graph contains a label (int) and a list
# (List[UndirectedGraphNode]) of its neighbors.
# There is an edge between the given node and each of
# the nodes in its neighbors.
#
# OJ's undirected graph serialization (so you can understand error output):
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
#
#
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
#
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def toString(self):
        return self.label

zero = UndirectedGraphNode(0)
one = UndirectedGraphNode(1)
two = UndirectedGraphNode(2)
zero.neighbors.extend([one, two])
one.neighbors.extend([two])
two.neighbors.extend([two])


def cloneGraph(node):
    visited = {}
    return cloneNode(node, visited)


def cloneNode(node, visited):
    if not node: return

    if node.label in visited.keys():
        return visited.get(node.label)

    clone = UndirectedGraphNode(node.label)
    visited.update({clone.label: clone})
    for neigh in node.neighbors:
        clone.neighbors.append(cloneNode(neigh, visited))

    return clone

cl = cloneGraph(zero)
# for n in cl.neighbors:
#     for k in n.neighbors:
#         print(k.label)