from flask import jsonify

def bad_request_error(e):
    return jsonify({'error': 'Bad Request - The request could not be understood'}), 400

def not_found_error(e):
    return jsonify({'error': 'Not Found - The requested URL was not found on the server'}), 404

def method_not_allowed_error(e):
    return jsonify({'error': 'Method Not Allowed - The method is not allowed for the requested URL'}), 405

def internal_server_error(e):
    return jsonify({'error': 'Internal Server Error - Something went wrong on the server'}), 500
