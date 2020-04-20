import random


class GridGraph():

    def __init__(self):
        #""" initializes a graph object and create a dictionary"""
        self.graph_dict = {}
        self.maze=[]


        #Adds a new GridNode to the graph with coordinates x and y.
    def addGridNode(self,x,y,node):
        if (x,y,node) not in self.graph_dict:
            self.graph_dict[(x,y,node)] = []

    # """This function adds an undirected edge"""
    def addUndirectedEdge(self,vert1,vert2):
            self.graph_dict[vert1].append(vert2[2])
            self.graph_dict[vert2].append(vert1[2])

        #"""This function removes an undirected edge"""
    def removeUndirectedEdge(self,vert1,vert2):
        if vert2[2] in self.graph_dict[vert1]:
            self.graph_dict[vert1].remove(vert2[2])
        if vert1[2] in self.graph_dict[vert1]:
            self.graph_dict[vert2].remove(vert1[2])


        #"""This returns a set of all Nodes in the graph"""
    def getAllNodes(self):
        return list(self.graph_dict.keys())
maze=None