from graph_model import GraphModeling

class GraphAlgorithms(GraphModeling):
    def bfs(self, start_node):
        """
        Explore la connectivité pour trouver toutes les pages accessibles.
        Utile pour identifier les 'Pages Isolées'
        """
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
        """
        Détecte les boucles de navigation (Cycles).
        Objectif clé du projet pour l'étude de la structure interne.
        """
        visited = set()
        rec_stack = set() # Pile de récursion pour suivre le chemin actuel

        def dfs_visit(node):
            visited.add(node)
            rec_stack.add(node)

            for neighbor in self.get_successors(node):
                if neighbor not in visited:
                    if dfs_visit(neighbor):
                        return True
                elif neighbor in rec_stack:
                    # Un cycle est détecté ici
                    return True

            rec_stack.remove(node)
            return False

        # On vérifie chaque nœud pour s'assurer de couvrir tout le graphe
        for node in self.nodes_info:
            if node not in visited:
                if dfs_visit(node):
                    return True
        return False