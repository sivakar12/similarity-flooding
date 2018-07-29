from similarityflooding.graph import Graph, Node, Edge, NodePair, EdgeType, PairwiseGraph

class TestPairwiseGraph:

    def test_create_graph(self):
        graph1 = Graph()
        node11 = Node('11')
        node12 = Node('12')
        edge1 = Edge(node11, node12, EdgeType('child'))
        graph1.add_nodes([node11, node12])
        graph1.add_edges([edge1])

        graph2 = Graph()
        node21 = Node('12')
        node22 = Node('22')
        edge2 = Edge(node21, node22, EdgeType('child'))
        graph2.add_nodes([node21, node22])
        graph2.add_edges([edge2])

        pairwise_graph = PairwiseGraph(graph1, graph2)

        assert len(pairwise_graph.nodes) == 2
        assert len(pairwise_graph.edges) == 1

        assert pairwise_graph.nodes == [NodePair(node11, node21), NodePair(node12, node22)]
        assert pairwise_graph.edges == [Edge(NodePair(node11, node21), NodePair(node12, node22), EdgeType('child'))]
