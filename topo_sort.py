# Copyright (c) 2018 Boris Popadiuk

# Written for New Beginnings Algorithms Winter 2018, Portland State University

class GraphEL(object):
    """Edgelist graph class. Written by Bart Massey and shared with students"""

    def __init__(self, nvertices, edges, directed=True):
        "Create an edge-list graph."
        self.nvertices = nvertices
        self.directed = directed
        if directed:
            self.edges = edges
        else:
            self.edges = set()
            for v1, v2 in edges:
                self.edges.add((v1, v2))
                self.edges.add((v2, v1))
            self.edges = list(self.edges)

    def undirected(self):
        "Return the undirected version of a directed edge-list graph."
        assert self.directed
        return GraphEL(self.nvertices, self.edges, directed=False)

    def toGraphAL(self):
        "Return the adjacency-list representation of an edge-list graph."
        return GraphAL(self.nvertices, self.edges, self.directed)

    def __repr__(self):
        return "GraphEL({}, {}, directed={})".format(
            self.nvertices,
            self.edges,
            self.directed
        )

    def __eq__(self, g):
        if type(g) is GraphAL:
            g = g.toGraphEL()
        if self.directed != g.directed:
            return False
        if self.nvertices != g.nvertices:
            return False
        return set(self.edges) == set(g.edges)

def kahn_toposort(graph):
    """Create topological sort of graph, return as list.
       Fail if cycle is detected."""

    edges = build_edge_dict(graph)
    no_incoming = build_no_incoming(graph)
    yes_incoming = [x for v in edges.values() for x in v]
    L = []

    while len(no_incoming) > 0:
        n = no_incoming.pop()
        L.append(n)
        if n not in edges.keys():
            continue
        for i in edges[n]:
            yes_incoming.remove(i)
            if i not in yes_incoming:
                no_incoming.add(i)
    if len(yes_incoming) > 0:
        print('ERROR: Cycle detected')
                
    return L 

def build_edge_dict(graph):
    """Create adjacency list representation of graph"""

    edge_dict = dict()
    for i, j in graph.edges:
        if i not in edge_dict:
            edge_dict[i] = [j]
        else:
            edge_dict[i].append(j)
    return edge_dict
                
def build_no_incoming(graph):
    """Compile set of vertices with no incoming edges"""

    no_incoming = set()
    yes_incoming = set()
    for i, j in graph.edges:
        yes_incoming.add(j)
    for i, j in graph.edges:
        if i not in yes_incoming:
            no_incoming.add(i)
    return no_incoming


cascadia_web_serv = GraphEL(11, [(1,2), (2,3), (2,10), (2,5), (9,3), (9,10), (9,5), (9,11), (7,5), (7,8), (3,4), (10,6), (5,6)])
topological_sort = kahn_toposort(cascadia_web_serv)
wiki_graph = GraphEL(8, [(5,11), (7, 11), (3, 8), (11, 2), (11, 9), (11, 10), (8, 9), (3,10), (7, 8)])
wiki_sort = kahn_toposort(wiki_graph)
print('topological sort of graph: ', cascadia_web_serv)
print(topological_sort)
print('wiki: ', wiki_sort)
