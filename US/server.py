from flask import Flask, request, jsonify
from socket import *
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    # make sure all parameters exist
    if hostname and fs_port and as_ip and as_port and number:
        client_socket = socket(AF_INET, SOCK_DGRAM)
        message = 'TYPE=A\nNAME={}'.format(hostname)
        client_socket.sendto(message.encode(), (as_ip, as_port))

        modified_message, server_address = client_socket.recvfrom(2048)
        client_socket.close()
        message_decoded = modified_message.decode()
        name, value = message_decoded.split()
        name = name.split('=')[1]
        value = value.split('=')[1]

        result = requests.get('http://{}:{}/fibonacci?number={}'.format(value, fs_port, number))

        return jsonify(result.json()), 200
    else:
        return jsonify("Bad request, missing parameters"), 400


app.run(
    host='0.0.0.0',
    port=8080,
    debug=True
)
