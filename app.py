from flask import Flask, jsonify, request, render_template
import os

print(os.getcwd())

app = Flask(__name__, template_folder='templates')

# Initial grid state and agent position
grid = [
    [' ', 'G', ' ', 'G'],
    ['W', ' ', 'P', ' '],
    ['S', 'T', ' ', ' '],
    [' ', ' ', 'P', 'W']
]
agent_position = (0, 0)  # Starting position of the agent


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-grid', methods=['GET'])
def get_grid():
    return jsonify({'grid': grid, 'agent_position': agent_position})


@app.route('/update-grid', methods=['POST'])
def update_grid():
    global grid, agent_position
    data = request.get_json()
    new_grid = data.get('grid')
    new_position = data.get('position')
    if new_grid:
        grid = new_grid
    if new_position:
        agent_position = tuple(new_position)
    return jsonify({'status': 'success', 'grid': grid, 'agent_position': agent_position})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
