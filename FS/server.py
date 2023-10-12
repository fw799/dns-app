from flask import Flask, request, jsonify
from socket import *

app = Flask(__name__)

def fibonacci_calculate(n):
    if n < 1:
        return 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_calculate(n - 1) + fibonacci_calculate(n - 2)
    
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if not number:
        return jsonify('Number is not provided'), 400
    return jsonify(fibonacci_calculate(int(number))), 200

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = int(data.get('as_port'))

    if hostname and ip and as_ip and as_port:
        client_socket = socket(AF_INET, SOCK_DGRAM)

        message = 'TYPE=A\nNAME={}\nVALUE={}\nTTL=10'.format(hostname, ip)
        client_socket.sendto(message.encode(), (as_ip, as_port))

        modified_message, server_address = client_socket.recvfrom(2048)
        client_socket.close()

        if modified_message.decode == 'Success':
            return jsonify('Success', 201)
        else:
            return jsonify('Failed')
    else:
        return jsonify('Bad request, missing parameters')


app.run(
    host='0.0.0.0',
    port=9090,
    debug=True
)

