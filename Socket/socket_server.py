from _ast import If
from _thread import *
from operator import eq
import os
import socket

HOST = '' // 라즈베리파이서버IP
PORT = // 접속할 PORT

def threaded(client_socket, addr): 

    print('Connected by :', addr[0], ':', addr[1])

    try:
        data = client_socket.recv(1024)

        print('Get Message ' + data.decode())

        client_socket.send(data)

    except:
        print('Exception by ' + addr[0],':',addr[1])

    client_socket.close()

def main():
    global HOST, PORT

# 소켓 초기화
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓 에러처리  
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print('server start')

    while True:

        print('wait')

        client_socket, addr = server_socket.accept()
        start_new_thread(threaded, (client_socket, addr))

    server_socket.close()

main()
