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
        if vert1 in self.graph_dict[vert2]:
            self.graph_dict[vert2].remove(vert1)

        #"""This returns a set of all Nodes in the graph"""
    def getAllNodes(self):
        return list(self.graph_dict.keys())
