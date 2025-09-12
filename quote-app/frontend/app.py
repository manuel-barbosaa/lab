from flask import Flask, render_template, make_response
import requests, os

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5001/quote")


@app.route("/")
def index():
    try:
        response = requests.get(BACKEND_URL, timeout=3)
        quote_data = (
            response.json()
            if response.status_code == 200
            else {"text": "Service busy.", "author": "System"}
        )
    except requests.exceptions.RequestException:
        quote_data = {"text": "An unexpected error occurred.", "author": "System"}

    rendered = render_template("index.html", quote=quote_data)
    resp = make_response(rendered)
    return resp


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
