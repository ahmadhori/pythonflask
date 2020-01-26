# importing Flask constructor from flask package
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/hi')
def hi():
    return "You are welcome"


@app.route('/json')
def json():
    student = dict(firstname="ahmad", lastname="houri")
    return jsonify(student)


@app.route('/add', methods=["POST"])
def add_two_nums():
    dataDic = request.get_json()
    if "x" not in dataDic:
        return "Error", 305
    x = dataDic["x"]
    y = dataDic["y"]

    retJSON = {
        "z": x+y
    }

    return jsonify(retJSON)


if __name__ == "__main__":
    app.run(debug=True)
