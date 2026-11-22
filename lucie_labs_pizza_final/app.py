import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "lucie_labs")

# Paste your Formspree endpoint URL here (or set FORMSPREE_URL in Render Environment Variables)
FORMSPREE_URL = os.environ.get("FORMSPREE_URL", "https://formspree.io/f/xrpqyepb")

PORTFOLIO_ITEMS = [
    {
        "tag": "ARCADE CABINET #1",
        "title": "Five Nights at Foxes Den",
        "description": "Original survival horror fan-game built on Scratch. Watch the cameras and survive the night shift!",
        "url": "https://scratch.mit.edu/projects/1241784771/",
        "button_text": "▶ Play on Scratch"
    },
    {
        "tag": "ARCADE CABINET #2",
        "title": "Foxes Den Funtime Pizza",
        "description": "Arcade pizzeria sequel packed with animatronic chaos and late-night scares.",
        "url": "https://scratch.mit.edu/projects/1279280806/",
        "button_text": "▶ Play on Scratch"
    },
    {
        "tag": "VHS MYSTERY #3",
        "title": "Red Snow Tape",
        "description": "Creepy analog-horror Scratch game inspired by lost 90s VHS tapes and winter mysteries.",
        "url": "https://scratch.mit.edu/projects/1279364385/",
        "button_text": "▶ Play on Scratch"
    },
    {
        "tag": "PRIVATE BACKROOM TECH",
        "title": "M.O.X.X",
        "description": "Private personal assistant coded just for Lucie—crunches math problems and fires up Spotify behind the counter.",
        "url": None,
        "button_text": "🔒 Private Lab Tool"
    }
]

@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        portfolio=PORTFOLIO_ITEMS,
        formspree_url=FORMSPREE_URL
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
