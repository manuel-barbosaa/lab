from flask import Flask, jsonify, make_response
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
    response = make_response(jsonify(quote))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
