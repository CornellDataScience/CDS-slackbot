from typing import Callable
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from config import BOT_TOKEN, APP_TOKEN

app = App(token=BOT_TOKEN)

# basically calls the bot when doing @slackbot
@app.event("app_mention")
def mention_handler(body: dict, say: Callable): 
    say("You asked me a question!")

if __name__ == "__main__":
    handler = SocketModeHandler(app, APP_TOKEN)
    handler.start()