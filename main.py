import praw

# Create a Reddit instance
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="your_user_agent"
)

# Fetch top posts from a subreddit
subreddit = reddit.subreddit("WallStreetBets")
for submission in subreddit.top(limit=5,time_filter="week"):
    print(f"Title: {submission.title}, Score: {submission.score}, Author: {submission.author}")
    print(submission.num_comments)
    