import praw
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.getenv("PASSWORD")
RID = os.getenv("RID")
RSECRET = os.getenv("RSECRET")


def login():
    print("[login=>login] logging in...")
    try:
        r = praw.Reddit(
            username=USERNAME,
            password=PASSWORD,
            client_id=RID,
            client_secret=RSECRET,
            user_agent="kramer by /u/haulhelper_bot",
        )
        print("[login=>success] logged in!")
    except praw.exceptions.PRAWException:
        print("[login=>login->exception] something went wrong...")
    return r
