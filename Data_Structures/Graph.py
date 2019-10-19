"""
Graph Implementation

This implementation uses a defaultdict with a GraphNode as the defaultfactory.
If a searched vertex does not exist, it will return a GraphNode object where
GraphNode.vertex = None

"""
from collections import defaultdict, deque

class GraphNode:
    def __init__(self, v=None):
        self.vertex = v
        self.adjacent = []
        self.visited = False  # for traversals

class Graph:
    def __init__(self, vertices=[], directed=False):
        self.adjList = defaultdict(GraphNode)
        self.isDirected = directed
        if vertices:
            for v in vertices:
                self.adjList[v].vertex = v

    def addEdge(self, start, dest):
        if not self.adjList[start].vertex:
            self.adjList[start].vertex = start

        if not self.adjList[dest].vertex:
            self.adjList[dest].vertex = dest

        self.adjList[start].adjacent.append(self.adjList[dest])

        if not self.isDirected:
            self.adjList[dest].adjacent.append(self.adjList[start])

        directed = 'Added edge {} -> {}'.format(start, dest)
        undirected = 'Added edge {} <-> {}'.format(start, dest)

        return directed if self.isDirected else undirected

    def removeEdge(self, start, dest):
        if start not in self.adjList.keys() or end not in self.adjList.keys():
            return 'Edge does not exist'

        for i in range(len(self.adjList[start].adjacent)):
            if self.adjList[start].adjacent[i].vertex == dest:
                del(self.adjList[start].adjacent[i])
                break

        if not self.isDirected:
            for i in range(len(self.adjList[dest].adjacent)):
                if self.adjList[dest].adjacent[i].vertex == start:
                    del(self.adjList[dest].adjacent[i])
                    break

        directed = 'Removed edge {} -> {}'.format(start, dest)
        undirected = 'Removed edge {} <-> {}'.format(start, dest)

        return directed if self.isDirected else undirected
        

    def BFS(self, start):
        if start not in self.adjList.keys():
            return 'Start vertex not in graph.'
        
        to_visit = [start]
        visited = []
        while to_visit:
            current = to_visit.pop(0)
            for v in self.adjList[current].adjacent:
                if v.vertex not in to_visit and v.vertex not in visited:
                    to_visit.append(v.vertex)
                    
            visited.append(current)

        return visited
                
    def DFS(self, start):
        if start not in self.adjList.keys():
            return 'Start vertex not in graph.'
        
        self.adjList[start].visited = True
        print(start)
        for v in self.adjList[start].adjacent:
            if not v.visited:
                self.DFS(v.vertex)

    def resetVisitation(self):
        for v in self.adjList.values():
            v.visited = False

    def pathExists(self, start, end):
        if start not in self.adjList.keys() or end not in self.adjList.keys():
            return False

        to_visit = deque(start)

        while to_visit:
            current = self.adjList[to_visit.popleft()]
            for v in current.adjacent:
                if v.vertex not in to_visit and not v.visited:
                    if v.vertex == end:
                        return True
                    else:
                        to_visit.append(v.vertex)
                        current.visited = True
                        
        return False
        
        

"""
Representation of:

A - B - E
|
C - D
|  /
 F
 
"""

g = Graph(['A', 'B', 'C', 'D', 'E', 'F'])
g.addEdge('A', 'B')
g.addEdge('B', 'E')
g.addEdge('A', 'C')
g.addEdge('C', 'D')
g.addEdge('C', 'F')
g.addEdge('F', 'D')



