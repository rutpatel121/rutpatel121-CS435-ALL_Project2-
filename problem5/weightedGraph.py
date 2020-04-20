import random
from copy import copy, deepcopy
import collections
import heapq
from collections import deque

class WeightedGraph():

    def __init__(self):
        #""" initializes a graph object and create a dictionary"""
        self.graph_dict = {}
        self.edges=[]
        self.n=0 #stores no. of nodes

    #This function adds a new node to the graph
    def addNode(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            self.n=self.n+1


    #This adds a directed edge between first and second node
    def addWeightedEdge(self,vert1,vert2,weight):
        test_graph = deepcopy(self.graph_dict)
        test_graph[vert1].append(vert2)
        is_valid, message = self.validate_acyclic(test_graph)
        if is_valid:
            self.graph_dict[vert1].append(vert2)
            self.edges.append((vert1,vert2,weight))

    def itervalues(self,d, **kw):
        return iter(d.values(**kw))

    #Returns a list of all nodes in the graph with no dependencies. Used to validate DAG
    def independent_nodes(self, graph):

        dependent_nodes = set(
            node for dependents in self.itervalues(graph) for node in dependents
        )
        return [node for node in graph.keys() if node not in dependent_nodes]


    #Returns a topological ordering of the DAG. Raises an error if this is not possible (graph is not valid)
    #Used to check either graph is acyclic or not after adding a new edge
    def topological_sort(self, graph):

        in_degree = {}
        for nodes in graph:
            in_degree[nodes] = 0

        for nodes in graph:
            for edges in graph[nodes]:
                in_degree[edges] += 1

        queue = deque()
        for nodes in in_degree:
            if in_degree[nodes] == 0:
                queue.appendleft(nodes)

        l = []
        while queue:
            nodes = queue.pop()
            l.append(nodes)
            for edges in graph[nodes]:
                in_degree[edges] -= 1
                if in_degree[edges] == 0:
                    queue.appendleft(edges)

        if len(l) == len(graph):
            return l
        else:
            raise ValueError('graph is not acyclic')


    # this function checks either DAG is valid or not after adding adge
    def validate_acyclic(self, graph):
        graph = graph if graph is not None else self.graph
        if len(self.independent_nodes(graph)) == 0:
            return (False, 'no independent nodes detected')
        try:
            self.topological_sort(graph)
        except ValueError:
            return (False, 'failed topological sort')
        return (True, 'valid')


    #This removes an directed edge between first and second
    def removeDirectedEdge(self,vert1,vert2,weight):
        if vert2 in self.graph_dict[vert1]:
            self.graph_dict[vert1].remove(vert2)
            self.edges.remove((vert1,vert2,weight))


    #This returns a set of all Nodes in the graph
    def getAllNodes(self):
        return list(self.graph_dict.keys())
weighted_graph=None