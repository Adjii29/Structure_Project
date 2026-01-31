from src.graph_model import GraphModeling

def main():
    # Initialisation de la partie d'Amine [cite: 13]
    fstt_graph = GraphModeling()
    fstt_graph.load_data('data/fstt_data.json')
    
    # Prêt pour les algorithmes d'Adjii [cite: 18]
    print("--- Prêt pour l'analyse du graphe ---")

if __name__ == "__main__":
    main()