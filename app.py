from flask import Flask, jsonify  # importing Flask constructor from flask package
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


if __name__ == "__main__":
    app.run(debug=True)
