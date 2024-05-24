from flask import Flask, request, jsonify

app = Flask(__name__)

access_tokens = {}
# In-memory storage for access tokens (for simplicity)
# in real life this value could come from an oauth server
valid_tokens = []

@app.route('/')
def server_status():
    print('Secured Server accessed')
    return 'Secured Server is running!'

# Listen for POST requests to this route
@app.route('/app/home', methods=['POST'])

def check_access_token(): 
   
    # Extract the Authorization header from the request
    access_token = request.headers.get('Authorization')
    
    print(f"Received access token: {access_token}")

    # Validate the access token
    # if access_token not in valid_tokens:
    #     return jsonify({'error': 'Invalid access token'}), 401
    
   
  

    # print(f"Number of valid tokens: {len(valid_tokens)}")

    for token in valid_tokens:
        print(f"Token: {token}")
    response = {
        'access': "granted",
        'token_type': 'Bearer',
        'expires_in': 3600
    }
    return jsonify(response)

# Start the Flask server
if __name__ == '__main__':
    print("Starting Secured server...")
    
    app.run(debug=True, host='127.0.0.1', port=5001)
