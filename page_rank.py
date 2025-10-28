import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import scipy as scipy

G = nx.DiGraph()
[G.add_node(k) for k in ["A", "B", "C", "D", "E", "F", "G"]]
G.add_edges_from(
[
('G','A'), ('A','G'), ('B','A'),
('C','A'), ('A','C'), ('A','D'),
('E','A'), ('F','A'), ('B','D'),
('D','F')
]
)
pos = nx.spiral_layout(G)
nx.draw(G, pos, with_labels = True, node_color="red")

pr1 = nx.pagerank(G)
print(pr1)
nx.draw(G, pos, nodelist=list(pr1.keys()), node_size=[round(v * 4000)
for
v in pr1.values()],
with_labels = True, node_color="red")