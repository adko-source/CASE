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
    print('OAuth Server accessed')
    return 'OAuthServer is running!'

@app.route('/oauth/token', methods=['POST'])
def token():
    # Extract client credentials and grant type from the request
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')
     # Extract grant type from query parameters
    grant_type = request.form.get('grant_type')
    # grant_type = request.args.get('grant_type')

    print(client_id)
    print(client_secret)
    print(grant_type)
    
    # Validate client credentials and grant type
    if (client_id != client_credentials['client_id'] or client_secret != client_credentials['client_secret'] or grant_type != client_credentials['grant_type']):
        return jsonify({'error': 'Authentication failed. Please check client_id, client_secret and grant_type'}), 401
    
    # Generate an access token
    access_token = str(uuid.uuid4())
    
    # Store the access token (in-memory storage for simplicity)
    access_tokens[access_token] = {
        'client_id': client_id,
        'token_type': 'Bearer',
        'expires_in': 3600  # Token validity period in seconds
    }
    
    # Return the access token
    response = {
        'access_token': access_token,
        'token_type': 'Bearer',
        'expires_in': 3600
    }

    json_response = jsonify(response)

    return json_response


if __name__ == '__main__':
    print("Starting OAuthserver...")
    app.run(debug=True)
