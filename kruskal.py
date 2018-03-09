# Copyright (c) 2018 Boris Popadiuk
# for New Beginnings Algorithms Winter 2018

from math import inf
from unionfind import setUnion
from graphweight_comparison import graphCompare

class GraphEL(object):
    """Graph Edge List Class, written and distributed to class by Bart Massey"""

    def __init__(self, nvertices, edges, directed=False):
        "Create an edge-list graph."
        self.nvertices = nvertices
        self.directed = directed
        if directed:
            self.edges = edges
        else:
            self.edges = set()
            for v1, v2, w in edges:
                self.edges.add((v1, v2, w)) 
                self.edges.add((v2, v1, w)) 
            self.edges = list(self.edges)
        self.vertices = set() 
        for v1, v2, w in self.edges:
            self.vertices.add(v1)
            self.vertices.add(v2)
        self.GraphAL = dict()
        for i in self.edges:
            if i[0] not in self.GraphAL:
                self.GraphAL[i[0]] = [(i[1], i[2])]
            else:
                self.GraphAL[i[0]].append((i[1], i[2]))
            
    def sortbyWeight(self):
        self.edges = sorted(self.edges, key=lambda edge: edge[2])

    def __repr__(self):
        return "GraphEL({}, {}, directed={})".format(
            self.nvertices,
            self.edges,
            self.directed
        )

def kruskal(graph):
    """Build a minimum spanning tree of graph using Kruskal's Algorithm. 
       Return as GraphEL object"""

    s = setUnion(graph.nvertices)
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

    treeGraph = GraphEL(len(vertices), treeEdgelist)
    return treeGraph


#def build_graphAL(graph):
#    """Convert graph edge list to adjacency list representation, 
#       return as dictionary"""
#
#    edge_dict = dict()
#    for i in graph.edges:
#        if i[0] not in edge_dict:
#            edge_dict[i[0]] = [(i[1], i[2])]
#        else:
#            edge_dict[i[0]].append((i[1], i[2]))
#    return edge_dict

#def build_cpy(graph):
#    """Convert graph edge list to adjacency list representation, 
#       return as dictionary"""
#
#    edge_dict = dict()
#    for i in graph.edges:
#        if i[0] not in edge_dict:
#            edge_dict[i[0]] = [[i[1], inf]]
#        else:
#            edge_dict[i[0]].append([i[1], inf])
#    return edge_dict

def process_file(fhand):
    """Build a GraphEL object from edges file pointed to by fhand"""

    edge_list = []
    vertices = set()
    for line in fhand:
        line = line.strip()
        line = line.rstrip(')')
        line = line.lstrip('(')
        words = line.split(', ')
        words[2] = float(words[2])
        edge_list.append(tuple(words))
    for item in edge_list:
        vertices.add(item[0])
        vertices.add(item[1])
    graph = GraphEL(len(vertices), edge_list)
    return graph
    
if __name__ == "__main__":
    fhand = open('amtrak.txt')
    myGraph = process_file(fhand)
    minSpanningtree = kruskal(myGraph)
    print('\n\nMINIMUM SPANNING TREE:\n\n')
    print(minSpanningtree)
    graphCompare(myGraph, minSpanningtree)
