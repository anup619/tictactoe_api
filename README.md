# Tic Tac Toe Game with Flask Error Handling and API

This project implements a simple Tic Tac Toe game in Python, complete with a Flask web application for playing the game. Additionally, error handling is provided using Flask's error response mechanisms.

## Files

### `main.py`

`main.py` contains the core logic for the Tic Tac Toe game and includes an API endpoint for obtaining the optimal move. The functions include:

- **`check_initial_state(board)`**: Checks whether the board is in the initial state.
- **`player(board)`**: Returns the player who has the next turn on the board.
- **`actions(board)`**: Returns a set of all possible actions available on the board.
- **`result(board, action)`**: Returns the board that results from making a move on the board.
- **`winner(board)`**: Determines the winner of the game, if there is one.
- **`terminal(board)`**: Returns true if the game is over, false otherwise.
- **`utility(board)`**: Returns the utility value for the current state of the board.
- **`minimax(board)`**: Finds the optimal action for the current player using the minimax algorithm.

The Flask application includes an API endpoint at `/optimalmove` that accepts a POST request with a JSON body containing a 3x3 matrix with either "X", "O", and null values. The response will be a JSON object with keys:

- **`message`**: A descriptive message about the result.
- **`next_player`**: The player who has the next turn on the board.
- **`optimal_move`**: The optimal move suggested by the AI.
- **`winner_player`**: The winner of the game, if there is one.

### `errors.py`

`errors.py` provides error handling functions using Flask. These functions return JSON responses with appropriate status codes for different HTTP errors:

- **`bad_request_error(e)`**: 400 Bad Request
- **`not_found_error(e)`**: 404 Not Found
- **`method_not_allowed_error(e)`**: 405 Method Not Allowed
- **`internal_server_error(e)`**: 500 Internal Server Error

### `tictactoe.py`

This file defines constants (`X`, `O`, `EMPTY`) and includes the core game logic shared between `main.py` and `errors.py`.

## API Usage

To use the API, send a POST request to `https://anup619.pythonanywhere.com/optimalmove` with a JSON body containing a 3x3 matrix in the "board" key. Example:

```json
{
  "board": [
    ["X", "O", null],
    [null, "X", null],
    ["O", null, "O"]
  ]
}
```

The response will be a JSON object with keys:

```json
{
  "message": null,
  "next_player": "X",
  "optimal_move": [0, 2],
  "winner_player": null
}
```

Feel free to explore, contribute, and provide feedback! Happy gaming and API testing!