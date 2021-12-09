graph = {'A' : ['B','C'], 'B' : ['D', 'E'], 'C' : ['F'], 'D' : [], 'E' : ['F'], 'F' : []}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node, "->", end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Raghav Soni A2305218217 7CSE-4X\n")
print("Graph:")
print(graph)
print("\nStarting Node: 'A'")
print("DFS Traversal: ")
dfs(visited, graph, 'A')
print("end")
