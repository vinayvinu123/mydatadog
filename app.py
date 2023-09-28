from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, vinay!'

@app.route('/metrics', methods=['POST'])
def get_metrics():
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

