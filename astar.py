def aStarAlgo(start_node, stop_node):
    sum1=1
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        sum1 = sum1 + g[m]
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Shortest Path found for graph: {}'.format(path))
            print('Cost: '+str(sum1))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Shortest Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {'S': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}
    return H_dist[n]
Graph_nodes = {
    'S': [('C', 3),('B', 4)],
    'B': [('E', 12),('F', 5),('S', 4)],
    'C': [('D', 7),('E', 10),('S', 3)],
    'D': [('E', 2),('C', 7)],
    'E': [('G', 5),('B', 12),('C', 10),('D', 2)],
    'F': [('G', 16),('B', 5)]
}
print("Chaitanya Malik A2305218259")
aStarAlgo('S', 'G')
