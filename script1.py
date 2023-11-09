import sys
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.G = nx.Graph()
        self.initialize_graph()

    def initialize_graph(self):
        # Initialize the full graph with all edges
        for i in range(self.V):
            self.G.add_node(i)
            for j in range(i + 1, self.V):
                if self.graph[i][j] != 0:
                    self.G.add_edge(i, j, weight=self.graph[i][j])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
        pos = nx.spring_layout(self.G)  # Compute layout here

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and not mstSet[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

            self.plot_graph(parent, mstSet, pos)  # Pass the layout here

        self.printMST(parent)
        plt.pause(5)

    def plot_graph(self, parent, mstSet, pos):
        plt.clf()
        nx.draw(self.G, pos, with_labels=True,
                font_weight='bold', node_color='lightblue')

        # Include edges in MST, skipping the root node with parent -1
        mst_edges = [(parent[i], i)
                     for i in range(1, len(parent)) if mstSet[i]]

        # Non-MST edges are all the other edges
        non_mst_edges = [(u, v) for u, v in self.G.edges() if (
            u, v) not in mst_edges and (v, u) not in mst_edges]

        nx.draw_networkx_edges(
            self.G, pos, edgelist=mst_edges, edge_color='r', width=2)
        nx.draw_networkx_edges(
            self.G, pos, edgelist=non_mst_edges, edge_color='black', width=1)

        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)

        # Correctly identify explored nodes
        explored_nodes = [i for i in range(self.V) if mstSet[i]]
        nx.draw_networkx_nodes(
            self.G, pos, nodelist=explored_nodes, node_color='red')

        plt.show(block=False)
        plt.pause(1)

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def update_graph(self):
        self.G.clear()
        for i in range(self.V):
            self.G.add_node(i)
            for j in range(i + 1, self.V):
                if self.graph[i][j] != 0:
                    self.G.add_edge(i, j, weight=self.graph[i][j])


# Sample Scenario
g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
g.update_graph()
g.primMST()
