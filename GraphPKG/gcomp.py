# Copyright (c) 2018 Boris Popadiuk
# Test the difference in total sum of edges between two graphs

def graphCompare(graph1, graph2):
    vSum1 = 0
    vSum2 = 0 
    edgeSum1 = 0
    edgeSum2 = 0
    weightSum1 = 0
    weightSum2 = 0
    for v in graph1.GraphAL:
        vSum1 += 1
        for neighbor, weight in graph1.GraphAL[v]:
            edgeSum1 += 1
            weightSum1 += weight
    for v in graph2.GraphAL:
        vSum2 += 1
        for neighbor, weight in graph2.GraphAL[v]:
            edgeSum2 += 1
            weightSum2 += weight
    
    edgeSum1 = edgeSum1 // 2
    edgeSum2 = edgeSum2 // 2
    bigEdge = max(edgeSum1, edgeSum2)
    weightSum1 = weightSum1 / 2
    weightSum2 = weightSum2 / 2
    bigWeight = max(weightSum1, weightSum2)
    weightDiff = abs(weightSum1 - weightSum2)
    edgeDiff = abs(edgeSum1 - edgeSum2)

    print('\nGraph 1: {} vertices, {} edges, {:.2f} total weight.'.format(vSum1, edgeSum1, weightSum1))
    print('Graph 2: {} vertices, {} edges, {:.2f} total weight.'.format(vSum2, edgeSum2, weightSum2))
    print('Weight Difference: {:.2f} -- {:.2f}% of original map'.format(
        weightDiff,
        100 * (weightDiff / bigWeight)))
    print('Edge Difference: {} -- {:.2f}% of original map\n'.format(
        edgeDiff,
        100 * (edgeDiff / bigEdge)))
