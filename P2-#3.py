import random

class Graph():

    def __init__(self):
        #""" initializes a graph object and create a dictionary"""
        self.graph_dict = {}

        #"""This adds a new node to the graph"""
    def addNode(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

        #"""This function adds an undirected edge"""
    def addUndirectedEdge(self,vert1,vert2):
        if vert2 not in self.graph_dict[vert1]:
            self.graph_dict[vert1].append(vert2)
        if vert1 not in self.graph_dict[vert2]:
            self.graph_dict[vert2].append(vert1)


        #"""This function removes an undirected edge"""
    def removeUndirectedEdge(self,vert1,vert2):
        if vert2 in self.graph_dict[vert1]:
            self.graph_dict[vert1].remove(vert2)
        if vert1 in self.graph_dict[vert1]:
            self.graph_dict[vert2].remove(vert1)

        #"""This returns a set of all Nodes in the graph"""
    def getAllNodes(self):
        return list(self.graph_dict.keys())
graph = Graph()
class GraphSearch():
    def dfs(self, start, goal, path, traversed):
        path.append(start)
        traversed.add(start)
        if start == goal:
            return 1
        for node in graph.graph_dict[start]:
            if node not in traversed:
                result = self.dfs(node, goal, path, traversed)
                if result is not None:
                    return path
        return None

    def dfsrec(self, start, goal, path=None):
        path = []
        traversed = set()
        return self.dfs( start, goal, path,traversed )


    #"""Iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order."""
    def dfsiter(self, start, goal,path=None):
        path = []
        traversed= set()
        stack = [start]
        while stack:
            forward = stack.pop()
            path.append(forward)
            if forward == goal:
                return path
            traversed.add(forward)
            connection = graph.graph_dict[forward]
            for node in reversed(connection):
                if node not in traversed:
                    stack.append(node)



    # """Recursively returns an List of the Nodes in the Graph in a valid Breadth-First Traversal order."""

    def bft(self,graph, queue, path, traversed):
        if len(queue) != 0:
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

class Main():

    # """Creates n random nodes with randomly assigned unweighted, bidirectional edges."""
    @staticmethod
    def createRandomUnweightedGraphIter(n):

        i = 1
        while i <= n:
            k = random.randrange(1, 5, 1)
            graph.addNode(i)
            if i >= 5:
                l = 0
                while l < k:
                    rand_node = random.randrange(1, i, 1)
                    graph.addUndirectedEdge(rand_node, i)
                    l = l + 1
            i = i + 1

    # """Creates a Graph with n nodes where each node only has an edge to the next node created."""
    @staticmethod
    def createLinkedList(n):
        if n > 0:
            linked_list.addNode(1)
            i = 2
            while i <= n:
                linked_list.addNode(i)
                linked_list.addUndirectedEdge(i - 1, i)
                i = i + 1

    @staticmethod
    def createLinkedList_10000(n=10000):
        if n > 0:
            linked_list_10000.addNode(1)
            i = 2
            while i <= n:
                linked_list_10000.addNode(i)
                linked_list_10000.addUndirectedEdge(i - 1, i)
                i = i + 1
    #"""Run a BFT recursively on a LinkedList"""
    @staticmethod
    def BFTRecLinkedList(link_list):
        return search.bftrec(link_list)

    # run a BFT iteratively on a LinkedList
    @staticmethod
    def BFTIterLinkedList(link_list):
        return search.bftiter(link_list)

if __name__ == "__main__":
    linked_list = Graph()
    search = GraphSearch()
    linked_list_10000 = Graph()
    main_obj=Main()

    main_obj.createLinkedList_10000()
    main_obj.createRandomUnweightedGraphIter(10)
    main_obj.createLinkedList(20)

    print("*****************Graphs*****************")
    print ()
    print ("graph adjacency list------>",graph.graph_dict)
    print ()
    print("DFSRec------>",search.dfsrec(2,8))
    print ()
    print("DFSIter------>",search.dfsiter(2,8))
    print ()
    print ("BFTRec------>",search.bftrec(graph))
    print ()
    print ("BFTIter------>",search.bftiter(graph))
    print ()
    graph=linked_list
    print("*****************Linked List*****************")
    print ()
    print("DFSRec------>",search.dfsrec(2,8))
    print ()
    print("DFSIter------>",search.dfsiter(2,8))
    print ()
    print ("BFTRec------>",search.bftrec(linked_list))
    print ()
    print ("BFTIter------>",search.bftiter(linked_list))
    print ()
    main_obj.createLinkedList(10000)
    print ("BFTIterLinkedList_10000----->",main_obj.BFTIterLinkedList(linked_list_10000))
    print()
    print ("BFTRecLinkedList_10000----->",main_obj.BFTRecLinkedList(linked_list))
    