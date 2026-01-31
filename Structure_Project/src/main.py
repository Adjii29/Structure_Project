from algorithms import GraphAlgorithms

def main():
    # --- PERSON 1: AMINE (Modeling & Loading) ---
    print("=== PERSON 1: DATA MODELING (AMINE) ===")
    fstt = GraphAlgorithms()
    # Loading the 30 pages from the JSON dataset
    fstt.load_data('data/fstt_data.json') 
    
    # Display the adjacency list to show the graph structure
    print("\nGraph Structure (Adjacency List):")
    fstt.display()
    print("-" * 40)

    # --- PERSON 2: ADJII (Algorithms & Results) ---
    print("\n=== PERSON 2: CORE ALGORITHMS (ADJII) ===")
    
    # 1. Reachability Analysis (BFS)
    # Explores the site from the Homepage (P0) to see what is reachable
    reachable_nodes = fstt.bfs("P0")
    total_nodes = len(fstt.nodes_info)
    
    print(f"Total pages in dataset: {total_nodes}")
    print(f"Total reachable pages from Home (P0): {len(reachable_nodes)}")
    
    # Identify if there are isolated pages for the report
    if len(reachable_nodes) < total_nodes:
        print(f"Analysis: {total_nodes - len(reachable_nodes)} isolated pages detected.")
    
    # 2. Cycle Detection (DFS)
    # Checks for navigation loops within the site structure
    print("\nChecking for navigation cycles...")
    if fstt.has_cycle():
        print("RESULT: Alert! Navigation loops (cycles) detected in the site.")
    else:
        print("RESULT: Success! No navigation loops detected.")
    print("-" * 40)

if __name__ == "__main__":
    main()