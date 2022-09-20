from flask import Flask, jsonify
from ec2_metadata import ec2_metadata
app = Flask(__name__)

@app.route("/")
def hello():
    return f'hello {ec2_metadata.private_ipv4}'

@app.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')