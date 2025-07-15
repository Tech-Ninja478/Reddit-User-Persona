# reddit_scraper.py
import praw
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import datetime

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username_from_url(url: str) -> str:
    # Example: https://www.reddit.com/user/kojied/
    parsed = urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    if len(path_parts) >= 2 and path_parts[0] == 'user':
        return path_parts[1]
    raise ValueError("Invalid Reddit user URL")

def get_user_data(username: str, limit=100):
    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for post in user.submissions.new(limit=limit):
            posts.append({
                'type': 'post',
                'title': post.title,
                'text': post.selftext,
                'subreddit': str(post.subreddit),
                'url': f"https://www.reddit.com{post.permalink}",
                'created': datetime.datetime.fromtimestamp(post.created_utc).isoformat()
            })

        for comment in user.comments.new(limit=limit):
            comments.append({
                'type': 'comment',
                'text': comment.body,
                'subreddit': str(comment.subreddit),
                'url': f"https://www.reddit.com{comment.permalink}",
                'created': datetime.datetime.fromtimestamp(comment.created_utc).isoformat()
            })

    except Exception as e:
        print(f"Error fetching user data: {e}")

    return {
        'username': username,
        'posts': posts,
        'comments': comments
    }
