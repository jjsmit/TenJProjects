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
                print('cout<< \n',data.decode())
                

                if not data:
                    print('no more data from', addr)
                    break

        finally:
            conn.close()


def send(conn):
    while True:
        message = input("cin>> \n")
        message = str.encode(message)
        conn.sendall(message)
        time.sleep(0.1)

def ComputeKey(conn):
    #Pick numbers for base, power and modulo
    Base = 7
    Number = 3
    Mod = 123

    #Compute Local public key
    PublicKey = str(Base**Number%Mod)

    #Combine base mod and local public key for sending and send to client
    Smessage = str(Base)+' '+str(Mod)+' '+str(PublicKey)
    message = str.encode(Smessage)
    conn.sendall(message)
    time.sleep(0.1)

    #Recieve public key client 
    Key = conn.recv(16)
    K = int(Key.decode())

    #Compute private key
    SecretKey = K**Number%Mod
    print(SecretKey)
    return (SecretKey)

try:
    create_server()
    conn, addr = s.accept()
    K = ComputeKey(conn)
    threading._start_new_thread( receive,(conn,addr))
    threading._start_new_thread( send, (conn,))

    while True:
        time.sleep(100)
    
except:
    print("exception")
