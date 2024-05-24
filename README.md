# CASE (Code Name)
# Tools 
-----
* Python 


# Description
------------
Creates a dummy OAuth and secured server for testing


# Instructions
1. Clone and open repository
2. Open terminal and cd into project directory
3. Enter `python -m venv venv` in terminal to create a virtual python environment. This installs packages to the local project only intsead of globally
4. Enter `venv\Scripts\activate` in terminal to activate the virtual environment
5. Enter `python -m pip install -r requirements.txt` in terminal to install dependencies
6. `python oauthserver.py` to start the test OAuth server
7. `python securedsurver.py` to start test secured server that
8. Use Postman or another similar app that can call http://127.0.0.1:5000/oauth/token
9. Send the following data as x-www-form-urlencoded
   * client_id
   * client_secret
   * grant_type
10. Match each of the above values with the same values within the client_credentials object in server.py
11. POST to endpoint


