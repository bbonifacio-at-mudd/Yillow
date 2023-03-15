# app.py
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-python-file')
def run_python_file():
    # Run your local Python file and capture its output
    command_output = subprocess.check_output(['python', '/Users/Brandon/Desktop/Yillow/app.py'])
    
    # Convert the output to a string and return it as JSON
    output_string = command_output.decode('utf-8').strip()
    return jsonify({'output': output_string})

if __name__ == '__main__':
    app.run()