import praw


# praw.ini should be in the same dir
reddit = praw.Reddit('redbot')

print(reddit.read_only)

for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)
