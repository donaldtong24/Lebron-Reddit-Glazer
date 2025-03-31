import praw
import time
import os


def authenicate():
    print("Authenicating...")
    reddit = praw.Reddit('lebronbot',user_agent="Lebron Glazer by /u/DTRedditBot")
    print("Authenicated as {}".format(reddit.user.me()))
    return reddit

def run_bot(reddit,comments_replied_to):
    print("Obtaining 25 comments...")



    for comment in reddit.subreddit('test').comments(limit=25):
        if "lebron" in comment.body.lower() and comment.id not in comments_replied_to and comment.author != reddit.user.me():
            print("String with \"lebron\" found in comment " + comment.id)
            comment.reply("Lebron James is the best! [Here](https://i.ytimg.com/vi/y59-J0Q9v2o/sddefault.jpg) is an image of the glorious king!")
            comments_replied_to.append(comment.id)

            with open("comments_replied_to.txt","a") as f:
                f.write(comment.id + "\n")
    print("Sleeping for 10 seconds...")
    #Sleep for 10 seconds
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt","r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)
                                       
    return comments_replied_to

comments_replied_to = get_saved_comments()
print (comments_replied_to)

def main():
    reddit = authenicate()
    while True:
        run_bot(reddit,comments_replied_to)

if __name__ == "__main__":
    main()