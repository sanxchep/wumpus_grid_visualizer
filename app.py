from flask import Flask, jsonify, request, render_template
import os

print(os.getcwd())

app = Flask(__name__, template_folder='templates')

# Initial grid state and agent position
grid = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'P', 'X', 'X', 'X', 'X', 'P', 'X', 'P', 'X', 'X', 'X'],
        ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', 'X', 'X'],
        ['X', 'X', 'X', 'W', 'X', 'X', 'X', 'X', 'X', 'X', 'G', 'X', 'X', 'X'],
        ['X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'T', 'X', 'X', 'X', 'X', 'X', 'X', 'W', 'X', 'X', 'X'],
        ['X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'S', 'X', 'X', 'X', 'X', 'X', 'X', 'T', 'X', 'X', 'X'],
        ['X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X'],
        ['X', 'X', 'X', ' ', 'W', ' ', ' ', 'T', 'G', 'G', ' ', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

agent_position = (6, 3)  # Starting position of the agent
run_id = "1234#234"
moves = 0
gold_collected = 0
gold_data = [
    {'pos': (3, 10), 'taken': True},  # Position (row 4, column 11), not taken
    {'pos': (9, 8), 'taken': True},   # Position (row 10, column 9), not taken
    {'pos': (9, 9), 'taken': False}    # Position (row 10, column 10), not taken
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-grid', methods=['GET'])
def get_grid():
    return jsonify({
        'grid': grid,
        'agent_position': agent_position,
        'run_id': run_id,
        'moves': moves,
        'gold_collected': gold_collected,
        'gold_data': gold_data
    })


@app.route('/update-grid', methods=['POST'])
def update_grid():
    global grid, agent_position, run_id, moves, gold_collected, gold_data
    data = request.get_json()
    new_grid = data.get('grid')
    new_position = data.get('position')
    new_run_id = data.get('run_id')
    new_moves = data.get('moves')
    new_gold_collected = data.get('gold_collected')
    new_gold_data = data.get('gold_data')

    if new_run_id:
        run_id = new_run_id
    if new_moves:
        moves = new_moves
    if new_gold_collected:
        gold_collected = new_gold_collected
    if new_grid:
        grid = new_grid
    if new_position:
        agent_position = tuple(new_position)
    if new_gold_data:
        gold_data = new_gold_data

    return jsonify({
        'status': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
