class Node:
    def __init__(self, name):
        if type(name) != str:
            raise ValueError
        
        self.name = name
    
    def __str__(self):
        return 'Node: "' + self.name + '"'
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.name == other.name

class EdgeType:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'EdgeType: "' + self.name + '"'
    
    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

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

    def __eq__(self, other):
        return self.source == other.source and self.destination == other.destination and self.edge_type == other.edge_type

    def __hash__(self):
        return hash(hash(self.source) + hash(self.destination) + hash(self.edge_type))
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()
    
    def add_nodes(self, nodes):
        self.nodes.update(nodes)
    
    def add_edges(self, edges):
        self.edges.update(edges)

class NodePair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return 'Node pair of ' + str(self.left) + ' and ' + str(self.right)

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(hash(self.left) + hash(self.right))

class PairwiseGraph:
    def __init__(self, graph_1, graph_2):
        self.nodes = set()
        self.edges = set()

        self.generate_pairwise_graph(graph_1, graph_2)

    def generate_pairwise_graph(self, graph_1, graph_2):
        for edge_1 in graph_1.edges:
            for edge_2 in graph_2.edges:
                if edge_1.edge_type == edge_2.edge_type:
                    source_node = NodePair(edge_1.source, edge_2.source)
                    dest_node = NodePair(edge_1.destination, edge_2.destination)
                    edge = Edge(source_node, dest_node, edge_1.edge_type)

                    if source_node not in self.nodes:
                        self.nodes.update([source_node])
                    if dest_node not in self.nodes:
                        self.nodes.update([dest_node])
                    self.edges.update([edge])
    
    def next_iteration(self):
        pass