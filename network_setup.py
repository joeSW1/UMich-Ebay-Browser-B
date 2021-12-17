import networkx as nx

G = nx.Graph()

# Category
categories = [
    G.add_node("hat"),
    G.add_node("mug"),
    G.add_node("sweatshirt"),
    G.add_node("t+shirt"),
    G.add_node("pin"),
    G.add_node("pennant")
]

# Condition
conditions = [
    G.add_node("new"),
    G.add_node("pre_owned")
]

# Reputation
reputations = [
    G.add_node("top_rated"),
    G.add_node("not_top_rated")
]

for i in G.nodes:
    G.nodes[i]['type'] = "category"
