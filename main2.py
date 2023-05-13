import networkx as nx

graph = nx.Graph()

nodes = list(range(5))
graph.add_nodes_from(nodes)

edges = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 4)]
graph.add_edges_from(edges)

nx.draw_networkx(graph, font_color="black")