import main
from collections import deque

class TopSort():

    @staticmethod
    def Kahns(graph):
        Sorted_List = []
        ZeroInDegreeVertex = []
        inDegree = {nodes: 0 for nodes in graph}

        for nodes in graph:
            for edges in graph[nodes]:
                inDegree[edges] += 1

        for nodeVal in inDegree:
            if (inDegree[nodeVal] == 0):
                ZeroInDegreeVertex.append(nodeVal)

        while ZeroInDegreeVertex:
            edges = ZeroInDegreeVertex.pop(0)
            Sorted_List.append(edges)

            for neighbour in graph[edges]:
                inDegree[neighbour] -= 1
                if (inDegree[neighbour] == 0):
                    ZeroInDegreeVertex.append(neighbour)

        return Sorted_List


    @staticmethod
    def mDFS(graph):
        order, enter, state = deque(), set(graph), {}

        def dfs(vertex):
            state[vertex] = 0
            for nodeVal in graph.get(vertex, ()):
                sk = state.get(nodeVal, None)
                if sk == 0: raise ValueError("cycle")
                if sk == 1: continue
                enter.discard(nodeVal)
                dfs(nodeVal)
            order.appendleft(vertex)
            state[vertex] = 1

        while enter: dfs(enter.pop())
        return list(order)

if __name__ == "__main__":
    main_obj= main.Main()
    DAG=main_obj.createRandomDAGIter(1000)
    sort=TopSort()

    print("****************Directed Acyclic Graph******************")
    print()
    print("Graph Adjacency List------>",DAG.graph_dict)
    print()
    print("Toplogical Sort Kahn’s Algorithm-------->",sort.Kahns(DAG.graph_dict))
    print()
    print("Toplogical Sort mDFS Algorithm------>",sort.mDFS(DAG.graph_dict))

