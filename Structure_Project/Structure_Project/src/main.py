from algorithms import GraphAlgorithms
from visualize import GraphVisualizer

def main():
    # --- PERSON 1: AMINE (Modeling & Loading) ---
    print("=== PERSON 1: DATA MODELING (AMINE) ===")
    fstt = GraphAlgorithms()
    # Loading the 30 pages from the JSON dataset
    # The ".." tells Python to go UP one folder, then look for the data folder
    fstt.load_data('../data/fstt_data.json')
    
    # Display the adjacency list to show the graph structure
    print("\nGraph Structure (Adjacency List):")
    fstt.display()
    print("-" * 40)

    # --- PERSON 2: ADJII (Algorithms & Results) ---
    print("\n=== PERSON 2: CORE ALGORITHMS (ADJII) ===")
    
    # 1. Reachability Analysis (BFS)
    reachable_nodes = fstt.bfs("P0")
    total_nodes = len(fstt.nodes_info)
    
    print(f"Total pages in dataset: {total_nodes}")
    print(f"Total reachable pages from Home (P0): {len(reachable_nodes)}")
    
    # --- ORPHAN ANALYSIS ---
    print("\n--- Orphan Page Detailed Analysis ---")
    orphan_ids = fstt.get_orphan_pages("P0")
    
    if orphan_ids:
        print(f"ALERT: {len(orphan_ids)} Orphan pages detected (Invisible to users).")
        for node_id in orphan_ids:
            page_name = fstt.nodes_info[node_id]['name']
            print(f" [!] Orphan Found: {page_name} ({node_id})")
    else:
        print("SUCCESS: Every page is reachable from the Homepage.")
    
    # 2. Cycle Detection (DFS)
    print("\n--- Navigation Loop Analysis ---")
    if fstt.has_cycle():
        print("RESULT: Alert! Navigation loops (cycles) detected in the site.")
        print("Note: This means users or search bots may get stuck in repeating paths.")
    else:
        print("RESULT: Success! No navigation loops detected.")

    # --- CENTRALITY ANALYSIS (WHO IS THE BOSS?) ---
    print("\n=== CENTRALITY ANALYSIS (IN-DEGREE) ===")
    centrality_results = fstt.get_centrality_report()
    
    print(f"{'Page Name':<25} | {'Links Pointing To It':<20}")
    print("-" * 50)
    
    # Show the Top 5 most central pages
    for node_id, count in centrality_results[:5]:
        page_name = fstt.nodes_info[node_id]['name']
        print(f"{page_name:<25} | {count:<20}")

    # --- DEAD END ANALYSIS (SINKS) ---
    print("\n=== DEAD END ANALYSIS (SINKS) ===")
    sink_ids = fstt.get_sink_pages()
    
    if sink_ids:
        print(f"Detected {len(sink_ids)} Dead End pages:")
        for node_id in sink_ids:
            page_name = fstt.nodes_info[node_id]['name']
            print(f" [!] Dead End: {page_name} ({node_id}) -> No outgoing links.")
    else:
        print("SUCCESS: No dead ends found. Every page leads somewhere else.")
    print("-" * 40)

    # --- SUMMARY & RECOMMENDATIONS ---
    print("\n" + "="*40)
    print("=== PROJECT SUMMARY & RECOMMENDATIONS ===")
    print("="*40)
    
    if orphan_ids:
        print("1. CRITICAL: The site has unreachable pages (Orphans).")
        print("   Recommendation: Add these pages to the main menu or the Sitemap (P28).")
    
    if fstt.has_cycle():
        print("2. WARNING: Cyclic paths found.")
        print("   Recommendation: Audit 'Actualités' (P15) and 'Avis' (P16) links to ensure they don't trap users.")
        
    print("3. STRUCTURE: The graph is currently sparse.")
    print("   Recommendation: Increase internal linking to distribute 'Page Authority' better.")
    print("="*40)

    # --- VISUALIZATION ---
    print("\n=== GENERATING VISUAL GRAPH MAP ===")
    viz = GraphVisualizer(fstt.nodes_info, fstt.adj_list)
    # Pass orphans and sinks to the visualizer for color-coding
    viz.draw(orphan_list=list(orphan_ids), sink_list=sink_ids)

if __name__ == "__main__":
    main()