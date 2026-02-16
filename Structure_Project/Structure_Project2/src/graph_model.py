import json

class GraphModeling:
    def __init__(self):
        # Représentation par Liste d'Adjacence 
        self.adj_list = {} 
        self.nodes_info = {}

    def load_data(self, file_path):
        """Charge les noeuds et arêtes depuis le JSON [cite: 14, 17]"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.nodes_info = data['nodes']
                self.adj_list = data['adjacencyList']
            print(f"Modélisation réussie : {len(self.nodes_info)} pages chargées.")
        except FileNotFoundError:
            print("Erreur : Fichier data/fstt_data.json introuvable.")

    def get_successors(self, node_id):
        """Donne les voisins pour"""
        return self.adj_list.get(node_id, [])

    def display(self):
        """Affiche la structure du graphe orienté [cite: 15]"""
        for node, targets in self.adj_list.items():
            name = self.nodes_info[node]['name']
            print(f"{name} ({node}) -> {targets}")

if __name__ == "__main__":
    # Test pour Amine
    model = GraphModeling()
    model.load_data('data/fstt_data.json')
    model.display()