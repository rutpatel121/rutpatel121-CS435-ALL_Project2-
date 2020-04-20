import random
from copy import copy, deepcopy
import collections
import heapq
from collections import deque
from weightedGraph import WeightedGraph

class Main():

    @staticmethod
    def createRandomCompleteWeightedGraph(n):
        graph=WeightedGraph()
        i=1
        while i<=n:
            graph.addNode(i)
            i=i+1
        l=1
        while l<=n:
            nodeVal=1+l
            while nodeVal<=n:
                w=random.randrange(1, 10, 1)
                graph.addWeightedEdge(l,nodeVal,w)
                nodeVal=nodeVal+1
            
            l=l+1
            #if (l != nodeVal):
                #return
        return graph

    @staticmethod
    def createLinkedList(n):
        graph = WeightedGraph()
        if n>0:
            graph.addNode(1)
            i=2
            while i<=n:
                graph.addNode(i)
                graph.addWeightedEdge(i-1,i,1)
                i=i+1
        return graph

    @staticmethod
    def shortestPath(edges, source, sink):
        # create a weighted DAG - {node:[(cost,neighbour), ...]}
        graph = collections.defaultdict(list)
        for l, secondNodeEdge, weightEdge in edges:
            graph[l].append((weightEdge, secondNodeEdge))
        # create a priority queue and hash set to store visited nodes
        queue, visited = [(0, source, [])], set()
        heapq.heapify(queue)
        # traverse graph with BFS
        while queue:
            (cost, node, path) = heapq.heappop(queue)
            # visit the node if it was not visited before
            if node not in visited:
                visited.add(node)
                path = path + [node]
                # hit the sink
                if node == sink:
                    return cost
                # visit neighbours
                for weightEdge, neighbour in graph[node]:
                    if neighbour not in visited:
                        heapq.heappush(queue, (cost + weightEdge, neighbour, path))
        return float("inf")

    @staticmethod
    def dijkstras(start):
        map_dic={}
        i=1
        while i<=weighted_graph.n:
            if i!=start:
                distance=Main.shortestPath(weighted_graph.edges, start, i)
                map_dic[(start,i)]=distance
            i=i+1
        return map_dic

if __name__ == "__main__":
    main_obj=Main()
    weighted_graph=main_obj.createRandomCompleteWeightedGraph(10)
    linked_list=main_obj.createLinkedList(10)



    print("****************Weighted Graph******************")
    print()
    print("Adjacency list 10 nodes------>",weighted_graph.graph_dict)# Print adjacency list of graph created by createRandomCompleteWeightedGraph() function
    print()
    print("Weighted Edge list------->",weighted_graph.edges) #Print list of edges and weights of graph created by createRandomCompleteWeightedGraph() function
    print()
    print("Dictionary Mapping------>",main_obj.dijkstras(3)) #Print dictionary mapping each Node node in the graph to the minimum value from start to get to node. Last part of 5
    print()
    print("*****************Linked List******************")
    print()
    print("Linked List Adjacency List------>",linked_list.graph_dict)
    print()
    print("Linked List Uniform Edges",linked_list.edges)