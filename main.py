import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import astar as astar
def create_graph(nodes):
    # Create an nx graph
    G = nx.Graph()
    # G.add_nodes_from(nodes)
    nx.draw(G, with_labels=True)
    plt.savefig("first.png")

    for node, edges in nodes.items():
        G.add_node(node)
        print(node)
        # print(edges)
        # print(node)
        # print(edges)
        # G.add_edges_from(edges)
        # nx.draw(G, with_labels=True)
        # plt.savefig("second.png")

        for edge, weight in edges:
            G.add_edge(edge, weight)
            # print(node)
            print(edge)
            print(weight)
            # add the node and edges to the nx graph
    nx.draw(G, with_labels=True)
    plt.savefig("third.png")
    return G

def find_shortest_path(start, end, nodes):
    path = 0
    # Make a varaible which calls create_graph
    # make a path variable which calls the astar function from networkx
    G = create_graph(nodes)
    print(nx.astar_path(G, start, end))
    # path = astar.(G, start, end, )

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
G = create_graph(nodes)

# plt.figure(figsize=(6,4))
nx.draw(G)
plt.savefig("lab.png")