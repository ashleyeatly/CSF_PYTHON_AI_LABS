import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import astar as astar


def create_graph(nodes):
    # Create an nx graph
    G = nx.Graph()
    print("start G.number_of_nodes() ", G.number_of_nodes())
    print("start G.number_of_edges() ", G.number_of_edges())
    print("start G.nodes ", G.nodes)
    print("start G.edges ", G.edges)
    # G.add_edge()
    for node, edges in nodes.items():
        print("node in nodes.items ", node)
        print("edges in nodes.items ", edges)
        G.add_node(node)
        print("outer loop add_node(node) G.number_of_nodes() ", G.number_of_nodes())
        print("outer loop add_node(node) G.number_of_edges() ", G.number_of_edges())
        print("outer loop add_node(node) G.nodes ", G.nodes)
        print("outer loop add_node(node) G.edges ", G.edges)
        for edge, weight in edges:
            # add the node and edges to the nx graph
            print("edge in edges ", edge)
            print("weight in edges ", weight)

            G.add_edge(node,edge, weight = weight)
            print("inner loop add_edge(edge, weight) G.number_of_nodes() ", G.number_of_nodes())
            print("inner loop add_edge(edge, weight) G.number_of_edges() ", G.number_of_edges())
            print("inner loop add_edge(edge, weight) G.nodes ", G.nodes)
            print("inner loop add_edge(edge, weight) G.edges ", G.edges)

    print("end G.number_of_nodes() ", G.number_of_nodes())
    print("end G.number_of_edges() ", G.number_of_edges())
    print("end .nodes ", G.nodes)
    print("end G.edges ", G.edges)
    print("SET")
    # print("list(G.adj['Cardiff')) ",list(G.adj[0]))
    for (u, v, wt) in G.edges.data('weight'):
        print(f"({u}, {v}, {wt:.3})")
    print("We are now analysing")
    return G

def find_shortest_path(start, end, nodes):
    path = 0
    # Make a varaible which calls create_graph
    # make a path variable which calls the astar function from networkx
    G = create_graph(nodes)
    print("astar_path ",nx.astar_path(G, start, end))
    print("shortest path ",nx.shortest_path(G, source=start, target=end, weight=None))
    print("shortest path ",nx.shortest_path(G, source=start, target=end, weight="weight", method='dijkstra'))
    print("shortest path ",nx.shortest_path(G, source=start, target=end, weight="weight", method='dijkstra'))
    print("shortest_path ",[p for p in nx.all_shortest_paths(G, source=start, target=end)])
    print("shortest_path ",[p for p in nx.shortest_simple_paths(G, source=start, target=end)])
    print("shortest_path ",[p for p in nx.all_simple_edge_paths(G, source=start, target=end)])
    print("shortest_path ", nx.shortest_path_length(G, source=start, target=end, weight="weight",method="dijkstra"))
    print("astar_path ",nx.astar_path(G, start, end, heuristic=None, weight="weight"))
    print("astar_path ",nx.astar_path_length(G, start, end, heuristic=None, weight="weight"))
    return path


nodes = {
    "Cardiff": [("Barry", 10.9), ("Caerphilly", 11.9)],
    "Swansea": [("Neath", 11.5), ("Llanelli", 14.1)],
    "Newport": [("Cwmbran", 10.1), ("Pontypool", 10.6)],
    "Wrexham": [],
    "Barry": [("Cardiff", 10.9), ("Penarth", 7.3)],
    "Cwmbran": [("Newport", 10.1), ("Pontypool", 6.2)],
    "Llanelli": [("Swansea", 14.1), ("Aberdare", 22.3)],
    "Neath": [("Swansea", 11.5), ("Aberdare", 21.8)],
    "Bridgend": [("Porthcawl", 8.5), ("Blackwood", 9.9)],
    "Pontypool": [("Newport", 10.6), ("Cwmbran", 6.2)],
    "Aberdare": [("Llanelli", 22.3), ("Neath", 21.8)],
    "Colwyn Bay": [("Rhyl", 10.3), ("Merthyr Tydfil", 91.6)],
    "Merthyr Tydfil": [("Rhymney", 21.1), ("Aberdare", 9.6)],
    "Rhyl": [("Colwyn Bay", 10.3), ("Wrexham", 21.1)],
    "Penarth": [("Barry", 7.3), ("Cardiff", 6.1)],
    "Caerphilly": [("Cardiff", 11.9), ("Blackwood", 8.4)],
    "Porthcawl": [("Bridgend", 8.5), ("Aberdare", 24.8)],
    "Blackwood": [("Bridgend", 9.9), ("Caerphilly", 8.4)],
    "Ebbw Vale": [("Merthyr Tydfil", 18.9), ("Tonypandy", 18.1)],
    "Tonypandy": [("Ebbw Vale", 18.1), ("Bridgend", 14.8)]
}

start = "Wrexham"
end = "Cardiff"

# call the find shortest path method, and print it out
find_shortest_path(start, end, nodes)
# G = create_graph(nodes)

# plt.figure(figsize=(6,4))
# nx.draw(G)
# plt.savefig("lab.png")