from flask import Flask, request, jsonify
import os
 
app = Flask(__name__)
 
@app.route('/files', methods=['GET'])
def list_files():
    """List files in the 'data' directory.

    This function retrieves the list of files located in the 'data'
    directory and returns it as a JSON response with an HTTP status code of
    200. It uses the `os.listdir` method to obtain the file names.

    Returns:
        tuple: A tuple containing the JSON representation of the list of files
        and the HTTP status code 200.
    """

    files = os.listdir('data')
    return jsonify(files), 200
 
@app.route('/files/<filename>', methods=['GET'])
def read_file(filename):
    """Read the content of a specified file.

    This function attempts to open and read the content of a file located in
    the 'data' directory. If the file is found, it returns the content along
    with the filename in a JSON response with a status code of 200. If the
    file does not exist, it returns a JSON response indicating that the file
    was not found with a status code of 404.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        tuple: A tuple containing a JSON response with the filename and content or an
            error message,
            along with the corresponding HTTP status code.
    """

    try:
        with open(f'data/{filename}', 'r') as file:
            content = file.read()
        return jsonify({"filename": filename, "content": content}), 200
    except FileNotFoundError:
        return jsonify({"message": "File not found"}), 404
 
@app.route('/files/<filename>', methods=['POST'])
def write_file(filename):
    """Write content to a specified file.

    This function retrieves content from a JSON request and writes it to a
    file with the given filename. The file is created in the 'data'
    directory. If the file is successfully written, a success message is
    returned in JSON format.

    Args:
        filename (str): The name of the file to which content will be written.

    Returns:
        Response: A JSON response indicating the success of the file write operation.
    """

    data = request.json.get("content", "")
    with open(f'data/{filename}', 'w') as file:
        file.write(data)
    return jsonify({"message": f"File {filename} written successfully"}), 200
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
