from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    try:
        with open('acc.txt', 'r') as file:
            line = file.readline().strip()
            if line:
                result = {"status": "success", "data": line}
                return jsonify(result)
            else:
                return jsonify({"status": "error", "message": "File is empty"})
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "File not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
