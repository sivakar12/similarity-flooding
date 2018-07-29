from similarityflooding.graph import Node, EdgeType, Edge, Graph

class TestNode:
    def test_create_node(self):
        node = Node("node name")
        assert str(node) == 'Node: "node name"'
    
class TestEdgeType:
    def test_create_edge_type(self):
        edge_type = EdgeType("edge type name")
        assert str(edge_type) == 'EdgeType: "edge type name"'

class TestEdge:
    def test_create_edge(self):
        node1 = Node("Node1")
        node2 = Node("Node2")
        edge_type = EdgeType("Type1")
        edge = Edge(node1, node2, edge_type)
        assert str(edge) == 'Edge from ' + str(node1) + ' to ' + str(node2) + ' with edge type ' + str(edge_type)

class TestGraph:
    def test_create_graph_class(self):
        graph = Graph()
        assert graph != None
    
    def test_graph_nodes_are_same(self):
        graph = Graph()
        node1 = Node('1')
        node2 = Node('2')
        graph.add_nodes([node1, node2])
        assert len(graph.nodes) == 2
        assert graph.nodes == [node1, node2]
        