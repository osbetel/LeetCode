import sys
from collections import defaultdict

class Graph:

    # Constructor 
    def __init__(self):

        # default dictionary to store graph 
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v, value):
        self.graph[u].append(v)

        # A function used by DFS

    def DFSUtil(self, v, visited):

        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        print(v, end=' ')

        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

                # The function to do DFS traversal. It uses

    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph))

        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def djikstra(self, start):
        # from start -> return a list of shortest paths to all other nodes
        unvisited = list(self.graph.keys())
        shortest_paths = dict(zip(unvisited, [sys.maxsize] * len(unvisited)))
        shortest_paths[start] = 0
        prev_paths = {}

        while unvisited:
            current_min_vertex = None
            for v in unvisited:
                if current_min_vertex == None:
                    current_min_vertex = v
                elif shortest_paths[v] < shortest_paths[current_min_vertex]:
                    current_min_vertex = v
                neighbors = self.graph[current_min_vertex]
                for n in neighbors:
                    tentative_value = shortest_paths[current_min_vertex] + graph.value(current_min_vertex, n)
                    if tentative_value < shortest_paths[n]:
                        shortest_paths[n] = tentative_value
                        # We also update the best path to the current node
                        prev_paths[n] = current_min_vertex
        return prev_paths, shortest_paths

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.DFS(2))
print(g.BFS(2))
g.djikstra(2)