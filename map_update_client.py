import requests
import json


def update_grid(new_grid, position, run_id, moves, gold):
    """
    Server URL: https://github.com/sanxchep/wumpus_grid_visualizer
    Start the server and open the URL in a browser to visualize the grid.

    Send a POST request to update the grid and the agent's position on the server.

    Args:
    new_grid (list of list of str): The new state of the grid to send to the server.
    position (tuple): The new position of the agent as a tuple (row_index, col_index).

    Returns:
    dict: Response from the server.
    """
    url = "http://localhost:5000/update-grid"
    headers = {'Content-Type': 'application/json'}
    payload = {
        'grid': new_grid,
        'position': position,
        'run_id': run_id,
        'moves': moves,
        'gold': gold
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()
