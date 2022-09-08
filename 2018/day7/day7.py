import re
from networkx import DiGraph, lexicographical_topological_sort

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

    graph = DiGraph()
    # PART 1
    for line in data:
        line_search = re.search(r'Step ([A-Z]) must be finished before step ([A-Z])', line)
        node = line_search[1]
        link_node = line_search[2]
        graph.add_edge(node, link_node)
    print(''.join(lexicographical_topological_sort(graph)))

    # PART 2
    for node in graph.nodes:
        graph.nodes[node]['work'] = 61 + ord(node) - ord('A')

    total_seconds = 0

    while graph.nodes:
        available_nodes = [node for node in graph.nodes if not graph.in_degree(node)]

        for worker, node in zip(range(5), available_nodes):
            graph.nodes[node]['work'] -= 1
            if not graph.nodes[node]['work']:
                graph.remove_node(node)
        total_seconds += 1
    print(total_seconds)
