from graph_model import GraphModeling

class GraphAlgorithms(GraphModeling):
    def bfs(self, start_node):
        """Explore connectivity to find all reachable pages."""
        visited = set()
        queue = [start_node]
        visited.add(start_node)
        
        while queue:
            current = queue.pop(0)
            for neighbor in self.get_successors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

    def has_cycle(self):
        """Detect navigation loops (Cycles)."""
        visited = set()
        rec_stack = set()

        def dfs_visit(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbor in self.get_successors(node):
                if neighbor not in visited:
                    if dfs_visit(neighbor): return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False

        for node in self.nodes_info:
            if node not in visited:
                if dfs_visit(node): return True
        return False
    #Matthews update below for calculating the isolated pages(orphans nodes like doctorat,mathematique etc)

    def get_orphan_pages(self, start_node="P0"):
        """Identifies pages that cannot be reached from the start_node."""
        all_pages = set(self.nodes_info.keys()) #self.nodes_info.keys idetify the pages(nodes e.g they are 30)
        reachable_pages = self.bfs(start_node)
        return all_pages - reachable_pages

    def get_centrality_report(self):
        """Counts incoming links for each page."""
        in_degree = {node_id: 0 for node_id in self.nodes_info}
        for source, targets in self.adj_list.items():
            for target in targets:
                if target in in_degree:
                    in_degree[target] += 1
        return sorted(in_degree.items(), key=lambda item: item[1], reverse=True)

    def get_sink_pages(self):
        """Identifies pages with no outgoing links."""
        sinks = []
        for node_id in self.nodes_info:
            if len(self.get_successors(node_id)) == 0:
                sinks.append(node_id)
        return sinks