from .graph_model import GraphModeling

class GraphAlgorithms(GraphModeling):
    
    # --- 1. REACHABILITY & ISOLATED PAGES (BFS) Uses QUEUES(PILES)---
    def get_reachability_report(self, start_node="P0"):
       
        visited = set()
        order = [] # To keep track of the order pages were found
        queue = [start_node]
        visited.add(start_node)
        
        while queue:
            current = queue.pop(0)
            order.append(current)
            for neighbor in self.get_successors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # Identify the orphans (nodes in the dataset NOT reached by BFS)
        all_nodes = set(self.nodes_info.keys())
        isolated = all_nodes - visited
        
        return {
            "reachable_count": len(visited),
            "isolated_count": len(isolated),
            "isolated_list": [self.nodes_info[n]['name'] for n in isolated],
            "bfs_order": order
        }

    # --- 2. CYCLE DETECTION (Advanced DFS / Tarjan) Uses Stacks(FILES)---
    def find_all_cycles(self):
        """
        Implementation of Tarjan's algorithm to find Strongly Connected Components (SCCs).
        Identifies exactly WHICH pages form navigation loops.
        """
        index_map = {}
        lowlink = {}
        stack = []
        on_stack = set()
        index_counter = 0
        sccs = []

        def strongconnect(v):
            nonlocal index_counter
            index_map[v] = index_counter
            lowlink[v] = index_counter
            index_counter += 1
            stack.append(v)
            on_stack.add(v)

            for w in self.get_successors(v):
                if w not in index_map:
                    strongconnect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif w in on_stack:
                    lowlink[v] = min(lowlink[v], index_map[w])

            if lowlink[v] == index_map[v]:
                component = []
                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    component.append(w)
                    if w == v: break
                sccs.append(component)

        for node in self.nodes_info:
            if node not in index_map:
                strongconnect(node)
        
        # Filter only components that are actual cycles (size > 1 or self-loop)
        cycles = [c for c in sccs if len(c) > 1 or (len(c) == 1 and c[0] in self.get_successors(c[0]))]
        return cycles

    # --- 3. CENTRAL PAGES (Degrees) ---
    def get_centrality_stats(self):
        """
        Calculates In-Degree and Out-Degree for every page.
        Matches the 'Top Hubs' section of the HTML.
        """
        stats = {}
        for node in self.nodes_info:
            out_deg = len(self.get_successors(node))
            # Count how many other nodes point TO this node
            in_deg = sum(1 for source in self.nodes_info if node in self.get_successors(source))
            
            stats[node] = {
                "name": self.nodes_info[node]['name'],
                "in_degree": in_deg,
                "out_degree": out_deg
            }
        return stats

    # --- 4. NAVIGATION SIMULATION (Shortest Path) ---
    def get_shortest_path(self, start, target):
        """
        BFS-based shortest path. Powers the 'Step' button in the simulation.
        """
        if start == target: return [start]
        queue = [[start]]
        visited = {start}

        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            for neighbor in self.get_successors(node):
                if neighbor == target:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None