# Copyright (c) 2018 Boris Popadiuk

# Implementation of A* Algorithm and Dijkstra's Algorithm
# For New Beginnings Algorithms Winter 2018

import math
from GraphPKG import UDG

KM_TO_MILES = 0.621371

def build_graphAL(graph):
    """Convert graph edge list to adjacency list representation, 
       return as dictionary"""

    edge_dict = dict()
    for i in graph.edges:
        if i[0] not in edge_dict:
            edge_dict[i[0]] = [(i[1], i[2])]
        else:
            edge_dict[i[0]].append((i[1], i[2]))
    return edge_dict

def reconstruct_path(start, end, parents):
    """Reconstruct minim path, return as list"""

    current = parents[end]
    path = []

    path.append(end)
    while current != None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path

def dijkstras_path(graph, start, end):
    """Find minimum path from start to end using Dijkstra's Algorithm"""

    ntries = 0
    closedSet = set()
    openSet = {node[0] for node in graph.edges} 
    graphAL = build_graphAL(graph)
    parents = {start:None}
    gScore = {node[0]:math.inf for node in graph.edges}
    gScore[start] = 0 
   
    while end not in closedSet:
        ntries += 1
        current = min(openSet, key=lambda node: gScore[node]) # set current to closest unvisited node
        for v, d in graphAL[current]:
            if v not in openSet: # skip nodes that have already been visited
                continue
            elif gScore[current] + d < gScore[v]: # if distance to v shorter through current node, set shortest path to v through current
                gScore[v] = gScore[current] + d
                parents[v] = current # record parent node of v
        closedSet.add(current) # update visited dictionary and remove current from unvisited
        openSet.remove(current)

    path = reconstruct_path(start, end, parents)
    print('Minimum path from ', start, ' to ', end, ': ', gScore[end], ' miles')
    print('path: ', path)
    print('Dijkstra\'s ntries: ', ntries)
    return True        

def aStar(graph, start, end):
    """Find minimum path from start to end using the A* algorithm with Euclidian admissible heuristic"""

    ntries = 0
    closedSet = set()
    openSet = {node[0] for node in graph.edges} 
    graphAL = build_graphAL(graph)
    parents = {start:None}
    gScore = {node[0]:math.inf for node in graph.edges}
    gScore[start] = 0 
    euclidDistances = get_euclid(open('./Data/am_euclidian.txt'), end)
    fScore = {node[0]:math.inf for node in graph.edges}
    fScore[start] = euclidDistances[start]

    while end not in closedSet:
        ntries += 1
        current = min(openSet, key=lambda node: fScore[node]) # set current to closest unvisited node
        for v, d in graphAL[current]:
            if v not in openSet: # skip nodes that have already been visited
                continue
            elif gScore[current] + d < gScore[v]: # set shortest path through current
                gScore[v] = gScore[current] + d
                fScore[v] = euclidDistances[v] + gScore[v]
                parents[v] = current # record parent node of v
        closedSet.add(current) # update visited dictionary and remove current from unvisited
        openSet.remove(current)

    path = reconstruct_path(start, end, parents)
    print('\nMinimum path from ', start, ' to ', end, ': ', gScore[end], ' miles')
    print('path: ', path)
    print('aStar ntries: ', ntries, '\n')
    return True

def process_file(fhand):
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
    graph = UDG.GraphEL(len(vertices), edge_list)
    return graph

def get_euclid(fhand, end):
    fScore = dict()
    fScore[end] = 0
    for line in fhand:
        line.strip()
        line = line.split()
        if line[0] == end:
            fScore[line[1]] = float(line[2]) * KM_TO_MILES
    return fScore

fhand = open('./Data/amtrak.txt')
graph = process_file(fhand)
aStar(graph, 'Emeryville', 'Raleigh')
dijkstras_path(graph, 'Emeryville', 'Raleigh')
