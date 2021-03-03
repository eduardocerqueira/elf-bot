import logging
import os
from slack_bolt import App

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL)

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

from commands import *

if __name__ == "__main__":
    app.start(3000)
    app.start(port=int(os.environ.get("PORT", 3000)))
