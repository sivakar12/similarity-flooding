class Node:
    def __init__(self, name):
        if type(name) != str:
            raise ValueError
        
        self.name = name
    
    def __str__(self):
        return 'Node: "' + self.name + '"'

class EdgeType:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'EdgeType: "' + self.name + '"'

class Edge:
    def __init__(self, source, destination, edge_type):
        if type(edge_type) != EdgeType:
            raise ValueError()
        if not (type(source) == Node or type(source) == NodePair):
            raise ValueError()
        if not (type(destination) == Node or type(destination) == NodePair):
            raise ValueError
        self.source = source
        self.destination = destination
        self.edge_type = edge_type
    
    def __str__(self):
        return 'Edge from ' + str(self.source) + ' to ' + str(self.destination) \
            + ' with edge type ' + str(self.edge_type)

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def add_nodes(self, nodes):
        self.nodes.extend(nodes)
    
    def add_edges(self, edges):
        self.edges.extend(edges)

class NodePair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return 'Node pair of ' + str(self.left) + ' and ' + str(self.right)
    
class PairwiseGraphNode:
    def __init__(self, graph_1, graph_2):
        self.nodes = []
        self.edges = []

        self.generate_pairwise_graph(graph_1, graph_2)

    def generate_pairwise_graph(self, graph_1, graph_2):
        pass
    
    def next_iteration(self):
        pass