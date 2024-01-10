from flask import request
from app import app
from fake_data.posts import post_data

# We will setup DB later, for now we will store all new users in this list
users = []

@app.route('/')
def index():
    first_name = 'Kadeeja'
    last_name = 'Griffin'
    age = 27
    return f'Hello World!! -- From {first_name} {last_name}'

#USER ENDPOINTS

# Create New User
@app.route('/users', methods=['POST'])
def create_user():
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    
    # Get the data from the request body
    data = request.json
    
    # Validate that the data has all of the required feilds
    required_fields = ['firstName', 'lastName', 'username', 'email', 'password']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
        if missing_fields:
            return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    # Get the values from the data
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    # Check to see if any current users already have that username and/or email
    for user in users:
        if user['username'] == username or user['email'] == email:
            return {'error': ' A user with that username and/or email already exists'}, 400
        
    # Create a new user dict and append to users list
    new_user = {
        "id": len(users) + 1,
        "firstName": first_name,
        "lastName": last_name,
        "username": username,
        "email": email,
        "password": password   
    }
    
    users.append(new_user)
    return new_user, 201

# POST ENDPOINTS

# get all posts
@app.route('/posts')
def get_posts():
    #Get the posts froom storage (fake data, will setup db tomorrow)
    posts = post_data
    return posts

# Get single post by ID 
@app.route('/posts/<int:post_id>')
def get_post(post_id): 
    #Get the posts from storage
    posts = post_data
    # For each dictionary in the list of post dictionaries
    for post in posts:
        #if the key of 'id' on the post dictionary mathced the post_id form teh URL
        return post
    # If we loop through all of the posts without returning, the post with that ID does not exist
    return{'error': f'Post with an ID of {post_id} does not exist'}, 404


#Create new Post route 
@app.route('/posts', methods=['POST'])
def create_post():
    #Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    required_fields = ["title", "body"]
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)}must be in the request body"}, 400
    
    # Get data from the body
    title = data.get('title')
    body = data.get('body')
    
    # Create a new post with data 
    new_post = {
        "id": len(post_data) + 1,
        "title": title,
        "body": body,
        "userId": 1,
        "dateCreated": "2024-01-09T11:25:45",
        "likes": 0
    }
    
    # Add the new post to the lost of posts
    post_data.append(new_post)
    return new_post, 201    
