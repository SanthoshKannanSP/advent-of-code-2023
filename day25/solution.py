import networkx as nx

def load():
    with open("input.txt","r") as f:
        data = f.read().strip().split("\n")

    return data
    
def solve(data):
    g = nx.Graph()

    for line in data:
        left, right = line.split(":")
        for node in right.strip().split():
            g.add_edge(left, node)
            g.add_edge(node, left)

    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)

    return len(a) * len(b)
    
if __name__ == "__main__":
    data = load()
    print(solve(data))