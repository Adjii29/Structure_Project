from flask import Flask, render_template, jsonify, request
from src.algorithms import GraphAlgorithms

app = Flask(__name__)
# Initialize your logic
fstt = GraphAlgorithms()
fstt.load_data('static/data/fstt_data.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-bfs')

def run_bfs():
    start_node = request.args.get('start', 'P0')
    # Change 'bfs' to 'get_reachability_report' and access ['bfs_order']
    report = fstt.get_reachability_report(start_node)
    return jsonify({"order": report['bfs_order']})


@app.route('/get-stats')
def get_stats():
    # We call the method from algorithms.py i
    stats = fstt.get_centrality_stats() 
    return jsonify(stats)

@app.route('/get-cycles')
def get_cycles():
    cycles = fstt.find_all_cycles()
    return jsonify({"cycles": cycles})

if __name__ == '__main__':
    app.run(debug=True)