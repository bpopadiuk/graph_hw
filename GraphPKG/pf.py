from GraphPKG import UDG

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
    graph = UDG.GraphEL(len(vertices), edge_list)
    return graph
