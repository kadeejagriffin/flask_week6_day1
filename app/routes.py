from app import app
from fake_data.posts import post_data

@app.route('/')
def index():
    first_name = 'Kadeeja'
    last_name = 'Griffin'
    age = 27
    return f'Hello World!! -- From {first_name} {last_name}'

# POST ENDPOINTS

# get all posts
@app.route('/posts')
def get_posts():
    #Get the pposts froom storage (fake data, will setup db tomorrow)
    posts = post_data
    return posts

# Get single post by ID 
@app.route('/posts/<int:post_id>')
def get_post(post_id): 
    #Get the posts from storage
    posts = post_data
    # nFor each dictionary in the list of post dictionaries
    for post in posts:
        #if the key of 'id' on the post dictionary mathced the post_id form teh URL
        return post
    # If we loop through all of the posts without returning, the post with that ID does not exist
    return{'error': f'Post with an ID of {post_id} does not exist'}, 404

@app.route('test/', methods=['POSTS'])
def test():
    return 'Hello'