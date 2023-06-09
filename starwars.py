# Gabasova, E. (2016). Star Wars social network. DOI: https://doi.org/10.5281/zenodo.1411479
#
# Simplified by Federico Albanese.
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

characters = ["R2-D2",
              "CHEWBACCA",
              "C-3PO",
              "LUKE",
              "DARTH VADER",
              "CAMIE",
              "BIGGS",
              "LEIA",
              "BERU",
              "OWEN",
              "OBI-WAN",
              "MOTTI",
              "TARKIN",
              "HAN",
              "DODONNA",
              "GOLD LEADER",
              "WEDGE",
              "RED LEADER",
              "RED TEN"]

edges = [("CHEWBACCA", "R2-D2"),
         ("C-3PO", "R2-D2"),
         ("BERU", "R2-D2"),
         ("LUKE", "R2-D2"),
         ("OWEN", "R2-D2"),
         ("OBI-WAN", "R2-D2"),
         ("LEIA", "R2-D2"),
         ("BIGGS", "R2-D2"),
         ("HAN", "R2-D2"),
         ("CHEWBACCA", "OBI-WAN"),
         ("C-3PO", "CHEWBACCA"),
         ("CHEWBACCA", "LUKE"),
         ("CHEWBACCA", "HAN"),
         ("CHEWBACCA", "LEIA"),
         ("CAMIE", "LUKE"),
         ("BIGGS", "CAMIE"),
         ("BIGGS", "LUKE"),
         ("DARTH VADER", "LEIA"),
         ("BERU", "LUKE"),
         ("BERU", "OWEN"),
         ("BERU", "C-3PO"),
         ("LUKE", "OWEN"),
         ("C-3PO", "LUKE"),
         ("C-3PO", "OWEN"),
         ("C-3PO", "LEIA"),
         ("LEIA", "LUKE"),
         ("BERU", "LEIA"),
         ("LUKE", "OBI-WAN"),
         ("C-3PO", "OBI-WAN"),
         ("LEIA", "OBI-WAN"),
         ("MOTTI", "TARKIN"),
         ("DARTH VADER", "MOTTI"),
         ("DARTH VADER", "TARKIN"),
         ("HAN", "OBI-WAN"),
         ("HAN", "LUKE"),
         ("C-3PO", "HAN"),
         ("LEIA", "MOTTI"),
         ("LEIA", "TARKIN"),
         ("HAN", "LEIA"),
         ("DARTH VADER", "OBI-WAN"),
         ("DODONNA", "GOLD LEADER"),
         ("DODONNA", "WEDGE"),
         ("DODONNA", "LUKE"),
         ("GOLD LEADER", "WEDGE"),
         ("GOLD LEADER", "LUKE"),
         ("LUKE", "WEDGE"),
         ("BIGGS", "LEIA"),
         ("LEIA", "RED LEADER"),
         ("LUKE", "RED LEADER"),
         ("BIGGS", "RED LEADER"),
         ("BIGGS", "C-3PO"),
         ("C-3PO", "RED LEADER"),
         ("RED LEADER", "WEDGE"),
         ("GOLD LEADER", "RED LEADER"),
         ("BIGGS", "WEDGE"),
         ("RED LEADER", "RED TEN"),
         ("BIGGS", "GOLD LEADER"),
         ("LUKE", "RED TEN")]

G_starWars = nx.Graph()

G_starWars.add_nodes_from(characters)
G_starWars.add_edges_from(edges)

print(G_starWars.nodes)
print(G_starWars.edges)

# plt.figure(figsize=(6,4))
# nx.draw(G_starWars)
nx.draw(G_starWars, with_labels = True)
plt.savefig("filename.png")
pos = nx.circular_layout(G_starWars)
nx.draw(G_starWars, pos=pos, with_labels = True)
plt.savefig("starwars2.png")

print(G_starWars.degree["LUKE"])
print(G_starWars.degree)

print(sorted(G_starWars.degree, key=lambda x: x[1], reverse=True))

pageranks = nx.pagerank(G_starWars) # A dictionary
print(pageranks["LUKE"])
print(sorted(pageranks, key=lambda x: x[1], reverse=True))
