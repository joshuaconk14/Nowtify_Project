# from flask import Flask, request, redirect, jsonify
# import requests
# import os
# from dotenv import load_dotenv

# # Load environment variables from a .env file (containing CLIENT_ID and CLIENT_SECRET)
# load_dotenv()


# # def: created app on Spotify Developer website, obtained app name, client_ID and client_secret
# app = Flask(__name__)

# CLIENT_ID = os.getenv('CLIENT_ID')
# CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# REDIRECT_URI = "https://Nowtify.com/callback"  # Adjust to your frontend URL

# # def: urls for spotify OAuth API
# SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
# SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
# SPOTIFY_API_URL = "https://api.spotify.com/v1"


# # initiating OAuth process
# # def
#     # scope: specifying app requests access to user private data, email, and top tracks/ artists
#     # url: url page to request scope access
#         # resp type=code: specifying app is requesting auth code for user
#         # REDIRECT_URI: URL path after user grants / denies access
# @app.route("/login")
# def login():
#     scope = "user-read-private user-read-email user-top-read"
#     auth_url = f"{SPOTIFY_AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scope}"
#     # user redicted to Spotify auth page, where user can grant / deny access
#     return redirect(auth_url)


# # the REDIRECT_URI url (/callback) after user grants / denies access
# #def
#         # code: retrieves query parameter code from URL that spotify sends user to after auth
#             # is used as temp token that can be exchanged for access token
#         # token_data: dict for required fields for POST request to spotify token URL
# @app.route("/callback")
# def callback():
#     code = request.args.get('code')
    
#     token_data = {
#         "grant_type": "authorization_code",
#         "code": code,
#         "redirect_uri": REDIRECT_URI,
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#     }
    
#     # def: POST request
#     token_response = requests.post(SPOTIFY_TOKEN_URL, data=token_data)
#     # turns token response into JSON format, easier for system to obtain info
#     token_json = token_response.json()
    
#     # def: extract access token from JSON response
#     access_token = token_json.get("access_token")
    
#     # def: Redirect back to the frontend with the access token in the query string
#     return redirect(f"https://Nowtify.com/?access_token={access_token}")


# # fetching user's spotify profile info
# # /me reps current user
# #def
#     #access_token: # Get access token from query parameters in URL that was sent back to the frontend
#         # frontend will send  token when making requests to /me endpoint
#         # used to request to Spotify's API to retrieve user prof info
#     #headers: where access token is included / stored
# @app.route("/me")
# def get_user_profile():
#     access_token = request.args.get('access_token')
    
#     if not access_token:
#         return jsonify({"error": "Access token is required"}), 400

#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     # def: GET request
#     response = requests.get(f"{SPOTIFY_API_URL}/me", headers=headers)
    
#     if response.status_code != 200:
#         return jsonify({"error": "Failed to fetch user data"}), response.status_code
    
#     #profile data returned in JSON msg
#     return jsonify(response.json())

# #running flask app
# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
