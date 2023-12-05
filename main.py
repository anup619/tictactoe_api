from flask import Flask, request, jsonify, abort
from tictactoe import minimax,player,X,O,EMPTY,winner,terminal,check_initial_state
from errors import bad_request_error, not_found_error, method_not_allowed_error, internal_server_error

app = Flask(__name__)   

@app.route('/')
def greet():
    return "Hello From tictactoe AI"

def validate_board_data(data):
    """
    Validate the data send in the request and returns appropriate error message
    """

    if 'board' not in data:
        return False, {'error': 'Board data not provided'}

    current_board = data['board']

    if not isinstance(current_board, list) or len(current_board) != 3 or not all(isinstance(row, list) and len(row) == 3 for row in current_board):
        return False, {'error': 'Invalid board format, must be a 2D array with 3 rows and 3 columns'}

    allowed_values = {X, O, EMPTY}
    if any(any(cell not in allowed_values for cell in row) for row in current_board):
        return False, {'error': 'Invalid cell value, must be "X", "O", or None'}

    return True, None

@app.route('/optimalmove', methods=['POST'])
def get_optimal_move():
    """
    Get the data from the request validates it and returns a json with next player and the optimal move for that player
    """
    try:
        if not request.data:
            return jsonify({'error': 'No data provided'}), 400

        if request.headers.get('Content-Type') != 'application/json':
            return jsonify({'error': 'Invalid content type, must be application/json'}), 400

        data = request.get_json()
        result = {
            'next_player' : None,
            'optimal_move' : None,
            'winner_player' : None,
            'message':None
        }

        valid, error_response = validate_board_data(data)
        if not valid:
            return jsonify(error_response), 400
        
        isinitalstate = check_initial_state(data['board'])
        if isinitalstate:
            result['next_player'] = X
            result['optimal_move'] = (0,1)
        else:
            isterminated = terminal(data['board'])
            if isterminated:
                winner_player = winner(data['board'])
                if winner_player:
                    result['winner_player'] = winner_player
                else:
                    result['message'] = 'game ended with a draw'
            else:
                result['next_player'] = player(data['board'])
                result['optimal_move'] = minimax(data['board'])

        return jsonify(result)

    except Exception as e:
        abort(500)  # Internal Server Error

@app.after_request
def add_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Referrer-Policy'] = 'same-origin'
    return response


app.register_error_handler(400, bad_request_error)
app.register_error_handler(404, not_found_error)
app.register_error_handler(405, method_not_allowed_error)
app.register_error_handler(Exception, internal_server_error)