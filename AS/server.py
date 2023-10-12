from socket import *
server_port = 53533

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind("", server_port)

mp = {}
while True:
    message, client_address = server_socket.recvfrom(2048)
    message_decoded = message.decode()

    if 'VALUE' in message_decoded:
        name, value = message_decoded.split('\n')
        name = name.split('=')[1]
        value = value.split('=')[1]
        
        mp[name] = value
        server_socket.sendto('Success'.encode, client_address)
    else:
        name = message_decoded.split('\n')[1].split('=')[1]
        if name in mp:
            response = 'TYPE=A\nNAME={}\nVALUE={}\nTTL=10'.format(name, mp[name])
            server_socket.sendto(response.encode(), client_address)
