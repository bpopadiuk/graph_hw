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
