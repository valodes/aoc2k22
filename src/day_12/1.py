import networkx as nx

with open("./src/day_12/input", "r") as infile:
    data = infile.read().splitlines()
    m = {}
    G = nx.DiGraph()

    for i, row in enumerate(data):
        for j, v in enumerate(row):
            m[(i, j)] = v

    target = [k for k in m.keys() if m[k] == "E"][0]
    start = [k for k in m.keys() if m[k] == "S"][0]
    m[target] = "z"
    m[start] = "s"

for (x, y) in m.keys():
    adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    adjacent = [p for p in adjacent if p in m.keys()]
    adjacent = [p for p in adjacent if (ord(m[p]) - ord(m[(x, y)])) <= 1]
    for a in adjacent:
        G.add_edge((x, y), a)

# part 1
result = nx.shortest_path(G, start, target)
print(len(result) - 1)