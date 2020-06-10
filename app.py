from flask import Flask, Response
import json
from client import prepare_to_tcp, tcp_handler
from flask import request, jsonify
app = Flask(__name__)


@app.route('/idm-example', methods=['POST'])
def idm_api():
    if request.method == 'POST':
        data = request.json
        fixed_length = prepare_to_tcp(data)
        mem = tcp_handler(fixed_length)
        return jsonify(mem)


if __name__ == "__main__":
    app.run(host='192.168.88.230', port=3333)
