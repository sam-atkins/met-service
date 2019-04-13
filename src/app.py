from flask import Flask, jsonify

app = Flask(__name__)

# TODO(sam) pull from config
DEBUG = True


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello world!!"})


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0")
