import praw

reddit = praw.Reddit(client_id='B-w6hy4i1uXMcnhIFMYY0g', client_secret='pr7MegU-3bft_Om26FUjlXpVX4p_MA', user_agent='Stock Search')
posts = []
data={}
ticker = 'TSLA'

ml_subreddit = reddit.subreddit('wallstreetbets')
for post in ml_subreddit.top(time_filter="month", limit = None):
    if ticker in post.title:
        posts.append([post.title, post.score, post.id, post.url, post.num_comments])

print(post)