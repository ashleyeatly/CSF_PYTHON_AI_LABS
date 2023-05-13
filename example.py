import networkx as nx
import matplotlib.pyplot as plt

# create a graph
G = nx.Graph()

# not much good yet as it has no nodes edges etc.
G.add_node("node 1")
G.add_nodes_from(["node 2", "node 3"])
G.add_nodes_from([("node 4", {"abc": 123}), ("node 5", {"abc": 0})])
print(G.nodes)
print(G.nodes["node 4"]["abc"]) # accessed like a dictionary

# But without edges between nodes, they’re isolated, and the dataset is no better than a simple table.

G.add_edge("node 1", "node 2")
G.add_edge("node 1", "node 6")
G.add_edges_from([("node 1", "node 3"),
                  ("node 3", "node 4")])
G.add_edges_from([("node 1", "node 5", {"weight" : 3}),
                  ("node 2", "node 4", {"weight" : 5})])

# The NetworkX library supports graphs like these, where each edge can have a weight. For example, in a social network graph where nodes are users and edges are interactions, weight could signify how many interactions happen between a given pair of users—a highly relevant metric.
#
# NetworkX lists all edges when using G.edges, but it does not include their attributes. If we want edge attributes, we can use G[node_name] to get everything that’s connected to a node or G[node_name][connected_node_name] to get the attributes of a particular edge:

print(G.nodes)
print(G.edges)
print(G["node 1"])
print(G["node 1"]["node 5"])

nx.draw(G)

weights = [1 if G[u][v] == {} else G[u][v]['weight'] for u,v in G.edges()]
nx.draw(G, width=weights)
plt.savefig("filename.png")