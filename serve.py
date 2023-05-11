import subprocess, socket
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_request():
  process = subprocess.Popen(["python3", "stress_cpu.py"])
  return str(process.pid)

@app.route('/', methods=['GET'])
def get_request():
  return socket.gethostname()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int("5000"))
