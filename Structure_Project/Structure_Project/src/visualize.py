import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:
    def __init__(self, nodes_info, adj_list):
        self.nodes_info = nodes_info
        self.adj_list = adj_list
        self.G = nx.DiGraph() # Directed graph to show link directions

    def build_networkx_graph(self):
        # Add all nodes to the graph
        for node_id, info in self.nodes_info.items():
            self.G.add_node(node_id, label=info['name'])
        # Add all directed edges (links)
        for source, targets in self.adj_list.items():
            for target in targets:
                self.G.add_edge(source, target)

    def draw(self, orphan_list=None, sink_list=None):
        self.build_networkx_graph()
        # k controls the distance between nodes; higher means more spread out
        pos = nx.spring_layout(self.G, k=0.8, seed=42)
        plt.figure(figsize=(14, 9))

        node_colors = []
        for node in self.G.nodes():
            if node == "P0": node_colors.append('gold')           # Homepage
            elif node in (orphan_list or []): node_colors.append('tomato') # Orphans
            elif node in (sink_list or []): node_colors.append('violet')   # Sinks
            else: node_colors.append('skyblue')                   # Normal

        # Smaller node_size to allow arrows to be seen
        nx.draw_networkx_nodes(self.G, pos, node_size=800, node_color=node_colors)
        
        # Enhanced edge drawing with visible arrows and margins
        nx.draw_networkx_edges(
            self.G, 
            pos, 
            width=1.2, 
            alpha=0.7, 
            arrowsize=25,       # Larger arrows for visibility
            arrowstyle='-|>',   # Solid arrowhead style
            min_source_margin=15, 
            min_target_margin=15,
            edge_color='gray'
        )
        
        # Draw labels with a slight offset or small font to avoid clutter
        labels = {node_id: info['name'] for node_id, info in self.nodes_info.items()}
        nx.draw_networkx_labels(self.G, pos, labels, font_size=8, font_family='sans-serif')

        plt.title("FSTT Website Graph Structure Analysis (Unidirectional Links)")
        plt.axis('off')
        
        # Add a legend for the report
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Home (P0)', markerfacecolor='gold', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Orphan (Unreachable)', markerfacecolor='tomato', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Sink (Dead End)', markerfacecolor='violet', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Normal Page', markerfacecolor='skyblue', markersize=10)
        ]
        plt.legend(handles=legend_elements, loc='upper right')
        
        plt.tight_layout()
        plt.show()