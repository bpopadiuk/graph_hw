# Copyright (c) 2018 Boris Popadiuk
# for New Beginnings Algorithms Winter 2018

from GraphPKG import unionfind, UDG, gcomp, pf

def kruskal(graph):
    """Build a minimum spanning tree of graph using Kruskal's Algorithm. 
       Return as GraphEL object"""

    s = unionfind.setUnion(graph.nvertices)
    graph.sortbyWeight()
    treeEdgelist = []
    vertices = list(graph.vertices)
    edgeDict = {vertices[i] : i + 1 for i in range(graph.nvertices)} # map edges to ints 1-45 to feed to setUnion structure

    for i in graph.edges:
        if not s.sameComponent(edgeDict[i[0]], edgeDict[i[1]]):
            print('edge: ' , i, ' in MST')
            treeEdgelist.append(i)
            s.unionSets(edgeDict[i[0]], edgeDict[i[1]])
        else:
            print('edge: ', i, 'would cause a cycle!')
        if len(treeEdgelist) == graph.nvertices - 1:
            break

    treeGraph = UDG.GraphEL(len(vertices), treeEdgelist)
    return treeGraph

if __name__ == "__main__":
    fhand = open('./Data/amtrak.txt')
    myGraph = pf.process_file(fhand)
    minSpanningtree = kruskal(myGraph)
    print('\n\nMINIMUM SPANNING TREE:\n\n')
    print(minSpanningtree)
    gcomp.graphCompare(myGraph, minSpanningtree)
