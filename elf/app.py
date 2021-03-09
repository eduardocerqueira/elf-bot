import logging
import os

from slack_bolt import App
from util import giphy_api_populate_list

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL)

# slack api waits for 3 second response, calling giphy api while building message back is to risky
# so builds a list with gifs from giphy during app loading and use as static data
gif_list = giphy_api_populate_list()
app = App(token=os.environ.get("SLACK_BOT_TOKEN"), signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))

# load slack commands as modules, must be after app is created
from commands import *

if __name__ == "__main__":
    app.start(3000)
    app.start(port=int(os.environ.get("PORT", 3000)))
