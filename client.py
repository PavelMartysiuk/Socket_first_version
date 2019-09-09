from socket import socket
def get_massage(word):
    client = socket()
    client.connect(('192.168.19.82', 5000))

    content = b""
    flag = True
    while True:
        if flag:
            number = word
            number = number.encode()
            client.send(number)
            flag = False

        massage = client.recv(1)
        if massage == b'~':
            break
        content += massage

    return(content.decode())
