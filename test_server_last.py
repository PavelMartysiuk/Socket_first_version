from socket import socket
from select import select
from os import listdir
from collections import defaultdict

books = listdir('./books/')
helpy = 0

server = socket()
server.bind(('192.168.100.2', 5000))
server.listen()

to_listen = defaultdict(list)
to_listen[server]

# send book vers = 2.0

while True:
    ready_to_read, ready_to_write, _ = select(to_listen, to_listen, [])
    for sock in ready_to_read:
        if sock is server:
            client, addr = server.accept()
            print(f'accept client {addr}')
            to_listen[client]
        else:
            try:
                number = sock.recv(3)
                print('message', number)
                number = number.decode()
                #number = int(number)
            except:
                print('error', number)
                del to_listen[sock]
                print('hit client,error read')
                continue
            try:
                if number == 'lis':
                    helpy+=1
                    all_books = ''
                    books = listdir('books')
                    all_books = all_books + ','.join(books)
                    all_books = all_books.encode()
                    print('Done',helpy)
                else:
                    number = int(number)
                    with open('./books/' + books[number]) as file:
                        content = file.read()
                    print(content[:30])
                    to_listen[sock].append(0)
                    to_listen[sock].append(content)
            
            except:
                print('error', number)
                del to_listen[sock]
                print('hit client,error in number operation')
                continue

    for cl in ready_to_write:
            if helpy == 1:
                cl.send(all_books)
                print('qq')
            if to_listen[cl]:
                index = to_listen[cl][0]
                sym = to_listen[cl][1][index]
                sym = sym.encode()
                to_listen[cl][0] += 1
                cl.send(sym)
                if to_listen[cl][0] >= len(to_listen[cl][1]):
                    del to_listen[cl]
                    sock.send(b'~')
                    sock.close()
