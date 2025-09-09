from flask import Flask, jsonify, request

app = Flask(__name__)

#                                        #
### APIs tested using "Thunder Client" ###
#                                        #

@app.route('/')
def home():
    return "<h1>This is the home page.</h1>"

@app.route('/api/hello', methods=['GET'])
def hello_world():
    # data = {
    #     'message': 'Hello, World!'
    # }
    # return jsonify(data), 200 # This is status code of json response. 200 means success/OK

    data = {
        'message': 'Error while loading'
    }
    return jsonify(data), 404 # This is status code of json response. 404 means not found

##### This code is using data from URL parameters
# @app.route('/api/addition/<int:a>/<int:b>', methods=['GET'])
# def addition(a,b):
#     result = a + b
#     data = {
#         'value': result,
#         'message': f"Addition of two numbers {a} and {b} is {result}"
#     }
#     return jsonify(data), 200
######


@app.route('/api/addition', methods=['GET'])
def addition():
    request_data = request.get_json()
    # print(type(request_data))
    # print(request_data)
    result_data = request_data['a'] + request_data['b']
    data = {
        'value': result_data,
        'message': f"Addition of two numbers {request_data['a']} and {request_data['b']} is {result_data}"
    }
    print(type(request_data))
    print(request_data)
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)





