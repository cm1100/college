



cost=['S',0]
global tree,heuristic

tree = {
    'S': [('C', 3),('B', 4)],
    'B': [('E', 12),('F', 5),('S', 4)],
    'C': [('D', 7),('E', 10),('S', 3)],
    'D': [('E', 2),('C', 7)],
    'E': [('G', 5),('B', 12),('C', 10),('D', 2)],
    'F': [('G', 16),('B', 5)]
}
heuristic = {'S': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}



closed =[]
opened =[['S',14]]
cost={'S':0}
while True:
    fn = [i[1] for i in opened]
    chosen_index = fn.index(min(fn))
    node = opened[chosen_index][0]
    closed.append(opened[chosen_index])
    del opened[chosen_index]
    if closed[-1][0] == 'G':
        break

    for item in tree[node]:
        if item[0] in [c[0] for c in closed]:
            continue

        cost.update({item[0]:cost[node]+item[1]})
        fn_node = cost[node]+heuristic[item[0]]+item[1]
        temp =[item[0],fn_node]
        opened.append(temp)
        print(f'opened :{opened}')
        print(f'cost : {cost}')

optimal_sequence=["G"]
print(closed)
trace_node='G'
for i in range(len(closed)-2,-1,-1):
    check_node = closed[i][0]
    if trace_node in [children[0] for children in tree[check_node]]:
        children_costs = [temp[1] for temp in tree[check_node]]
        children_nodes = [temp[0] for temp in tree[check_node]]

        if cost[check_node]+ children_costs[children_nodes.index(trace_node)] == cost[trace_node] :
            optimal_sequence.append(check_node)
            trace_node=check_node


optimal_sequence.reverse()

print(optimal_sequence)

