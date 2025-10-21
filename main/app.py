from flask import Flask, request, jsonify

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Health check route
@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

# Simple POST endpoint
@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    return jsonify({"received": data}), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
