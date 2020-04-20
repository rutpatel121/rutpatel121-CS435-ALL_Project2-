from main import *
from graph import *

graph = Graph()
class GraphSearch():
    def dfs(self, graph, start, goal, path, traversed):
        path.append(start)
        traversed.add(start)
        if start == goal:
            return 1
        for node in graph.graph_dict[start]:
            if node not in traversed:
                result = self.dfs(graph, node, goal, path, traversed)
                if result is not None:
                    return path
        return None

    def dfsrec(self, graph, start, goal, path=None):
        path = []
        traversed = set()
        return self.dfs(graph, start, goal, path, traversed)


    #"""Iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order."""
    def dfsiter(self, graph, start, goal,path=None):
        path = []
        traversed= set()
        stack = []
        stack.append(start)
        while len(stack):
            forward = stack.pop()
            path.append(forward)
            if forward == goal:
                return path
            traversed.add(forward)
            for node in reversed(graph.graph_dict[forward]):
                if node not in traversed:
                    stack.append(node)

    # """Recursively returns an List of the Nodes in the Graph in a valid Breadth-First Traversal order."""

    def bft(self,graph, queue, path, traversed):
        while len(queue):
            forward = queue.pop(0)
            path.append(forward)
            for connection in graph.graph_dict[forward]:
                if connection not in traversed:
                    queue.append(connection)
                    traversed.add(forward)
            return self.bft(graph, queue, path, traversed)
    def bftrec(self,graph):
        path = []
        traversed = set()
        for vertix in graph.graph_dict:
            if vertix not in traversed:
                self.bft(graph, [vertix], path, traversed)
        return path
    #""" Iteratively returns an List of all of the Nodes in the Graph in a valid Breadth-First Traversal."""
    def bfti(self,graph, queue, path, traversed):
        while len(queue) != 0:
            forward = queue.pop(0)
            path.append(forward)
            for vertix in graph.graph_dict[forward]:
                if vertix not in traversed:
                    traversed.add(vertix)
                    queue.append(vertix)
    def bftiter(self,graph):
        path= []
        traversed = set()
        for vertix in graph.graph_dict:
            if vertix not in traversed:
                self.bfti(graph, [vertix], path, traversed)
        return path
