from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Flask with tox!"})

if __name__ == "__main__":
    app.run(debug=True)
