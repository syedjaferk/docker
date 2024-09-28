from flask import Flask, request, jsonify
import os
 
app = Flask(__name__)
 
@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir('data')
    return jsonify(files), 200
 
@app.route('/files/<filename>', methods=['GET'])
def read_file(filename):
    try:
        with open(f'data/{filename}', 'r') as file:
            content = file.read()
        return jsonify({"filename": filename, "content": content}), 200
    except FileNotFoundError:
        return jsonify({"message": "File not found"}), 404
 
@app.route('/files/<filename>', methods=['POST'])
def write_file(filename):
    data = request.json.get("content", "")
    with open(f'data/{filename}', 'w') as file:
        file.write(data)
    return jsonify({"message": f"File {filename} written successfully"}), 200
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
