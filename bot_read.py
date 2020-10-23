#! /usr/bin/python

import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("linux")

for submission in subreddit.hot(limit=20):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
