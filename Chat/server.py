
import socket
import sys
import threading
import time

HOST = ''
PORT = 8002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')


def create_server():
    try:
        s.bind((HOST, PORT))
    except (socket.error) as msg:
        print ('Bind Failed', +str(msg[0]), 'Message', + msg[1])
        sys.exit()
        
    s.listen(1)


def receive(conn , addr):
        try:
            while True:
                time.sleep(0.1)
                data = conn.recv(16)
                print('recieved: ', data.decode())
                

                if not data:
                    print('no more data drom', addr)
                    break

        finally:
            conn.close()


def send(conn):
    while True:
        message = input("send>> ")
        message = str.encode(message)
        conn.sendall(message)
        time.sleep(0.1)

try:
    create_server()
    conn, addr = s.accept()
    threading._start_new_thread( receive,(conn,addr))
    threading._start_new_thread( send, (conn,))

    while True:
        time.sleep(100)
    
except:
    print("exception")