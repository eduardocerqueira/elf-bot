from app import app


@app.command("/test")
def test(ack, say):
    ack()
    say(f"elf is working!")
