from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Welcome to the simple web app!")

@app.route("/add", methods=["GET"])
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify(result=a + b)
    except ValueError:
        return jsonify(error="Invalid input"), 400

if __name__ == "__main__":
    app.run(debug=True)