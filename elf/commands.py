import json
import random

from app import app
from app import gif_list


@app.command("/test")
def test(ack, say):
    ack()
    say("elf is working!")


@app.command("/testday")
def test_day(ack, say, client, body, logger):
    ack()
    with open("data/testday.json") as f:
        data = json.load(f)

    if "blocks" not in data or len(data["blocks"]) == 0:
        say("I couldn't find any testday scheduled yet")
        return

    # set giphy image
    data["blocks"][1]["accessory"]["image_url"] = random.choice(gif_list)
    res = client.views_open(trigger_id=body["trigger_id"], view=json.dumps(data))
    logger.info(res)
