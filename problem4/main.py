from collections import deque
from directedGraph import DirectedGraph
import topSort

class Main():

    #Creates n random nodes with randomly assigned unweighted, directed edges.
    @staticmethod
    def createRandomDAGIter(n):
        graph = DirectedGraph()
        i=1
        nodeVal=1
        graph.addNode(1)
        while nodeVal<=n:
            if nodeVal+1<=n:
                graph.addNode(nodeVal+1)
            if nodeVal+2<=n:
                graph.addNode(nodeVal+2)
            if nodeVal+3<=n:
                graph.addNode(nodeVal+3)
            for l in range(3):
                nodeVal = nodeVal + 1
                if nodeVal<=n:
                    graph.addDirectedEdge(i,nodeVal)

            i=i+1
        return graph
        
if __name__ == "__main__":
    main_obj=Main()
    DAG=main_obj.createRandomDAGIter(1000)
    sort= topSort.TopSort()

    print("****************Directed Acyclic Graph******************")
    print()
    print("Graph Adjacency List------>",DAG.graph_dict)
    print()
    print("Toplogical Sort Kahn’s Algorithm-------->",sort.Kahns(DAG.graph_dict))
    print()
    print("Toplogical Sort mDFS Algorithm------>",sort.mDFS(DAG.graph_dict))
