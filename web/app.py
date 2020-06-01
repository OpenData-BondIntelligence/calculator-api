import flask
from flask import request, jsonify
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True
results = []


@app.route('/', methods=['GET'])
def home():
    return jsonify(results[-10:][::-1])


@app.route('/allresults', methods=['GET'])
def all_results():
    return jsonify(results)


@app.route('/operate', methods=['GET'])
def operate():

    if request.args is not None:
        operation = request.args['operation']
    else:
        return "Invalid operation parameters."
    result = 0
    # Check for the operation type and get the result
    if '+' in operation:
        operatee = operation.split('+')
        result = int(operatee[0]) + int(operatee[1])
    if '-' in operation:
        operatee = operation.split('-')
        result = int(operatee[0]) - int(operatee[1])
    if '*' in operation:
        operatee = operation.split('*')
        result = int(operatee[0]) * int(operatee[1])
    if '/' in operation:
        operatee = operation.split('/')
        result = int(operatee[0]) / int(operatee[1])
    results.append({
        "updated_date": datetime.now(),
        "operation": operation,
        "result": result
    })
    return jsonify(f"The most recent calculation is : {result}")


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'response_code': 404, 'response': 'This page does not exist'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
