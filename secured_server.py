from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for client credentials and access tokens (for simplicity)
client_credentials = {
    'client_id': 'ZOnlbEgkN8MABZ0c8FZfg-0o',
    'client_secret': 'UOW_x9gNvG1TaZTYkAIgmdTW1QsRLewROPO3vxLO64_5hSNT',
    'grant_type': 'client_credentials'
}

access_tokens = {}

@app.route('/')
def server_status():
    print('Secured Server accessed')
    return 'Secured Server is running!'

@app.route('/app/home', methods=['POST'])
def check_access_token(): 
    
    # Extract the Authorization header from the request
    access_token = request.headers.get('Authorization')
    
    print(access_token)

    response = {
        'access_token': access_token,
        'token_type': 'Bearer',
        'expires_in': 3600
    }
    return jsonify(response)


if __name__ == '__main__':
    print("Starting Secured server...")
    app.run(debug=True, host='127.0.0.1', port=5001)
