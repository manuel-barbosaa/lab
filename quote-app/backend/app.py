from flask import Flask, jsonify
import json
import random

app = Flask(__name__)


def load_quotes():
    with open("quotes.json", "r") as f:
        return json.load(f)


@app.route("/quote")
def get_quote():
    quotes = load_quotes()
    quote = random.choice(quotes)
    return jsonify(quote)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
