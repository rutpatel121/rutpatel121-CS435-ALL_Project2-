import random

from graph import Graph
from graphsearch import *

class Main():
    # """Creates n random nodes with randomly assigned unweighted, bidirectional edges."""
    @staticmethod
    def createRandomUnweightedGraphIter(n):
        graph = Graph()
        numbers = list(range(n))
        for i in numbers:
            graph.addNode(i)
        random.shuffle(numbers)
        for node in graph.graph_dict:
            e = random.randint(0, n-1)
            random.shuffle(numbers)
            for i in numbers[:e]:
                if i != node:
                    graph.addUndirectedEdge(node, i)
        return graph

    @staticmethod
    def createLinkedList(n):
        linked_list = Graph()
        for i in range(n):
            linked_list.addNode(i)
            if i != 0:
                linked_list.addUndirectedEdge(i - 1, i)
        return linked_list

    #"""Run a BFT recursively on a LinkedList"""
    @staticmethod
    def BFTRecLinkedList(linked_list):
        return search.bftrec(linked_list)

    # run a BFT iteratively on a LinkedList
    @staticmethod
    def BFTIterLinkedList(linked_list):
        return search.bftiter(linked_list)

if __name__ == "__main__":
    main_obj = Main()
    search = GraphSearch()
    g = main_obj.createRandomUnweightedGraphIter(10)
    gph = main_obj.createLinkedList(20)
    createLinkedList_graph = Graph()

    print("*****************Graphs*****************")
    print ()
    print("DFSRec------>",search.dfsrec(g, 2,8))
    print ()
    print("DFSIter------>",search.dfsiter(g, 2,8))
    print ()
    print ("BFTRec------>",search.bftrec(g))
    print ()
    print ("BFTIter------>",search.bftiter(g))
    print ()
    print("*****************Linked List*****************")
    print ()
    print("DFSRec------>",search.dfsrec(gph, 2,8))
    print ()
    print("DFSIter------>",search.dfsiter(gph, 2,8))
    print ()
    print ("BFTRec------>",search.bftrec(gph))
    print ()
    print ("BFTIter------>",search.bftiter(gph))
    print ()
    #main_obj.createLinkedList(10000)
    graphRec = main_obj.createLinkedList(100)
    graphIter = main_obj.createLinkedList(10000)
    recGraph = main_obj.BFTRecLinkedList(graphRec) 
    iterGraph = main_obj.BFTIterLinkedList(graphIter)
    print ("BFTRecLinkedList_10000----->",(iterGraph))
    print()
    print ("BFTIterLinkedList_10000----->",(recGraph))