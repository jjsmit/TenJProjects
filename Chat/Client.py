import socket
import sys
import threading
import time


def create_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ('socket created')
        host = '127.0.0.1'
        port = 8002
        remote_ip = socket.gethostbyname(host)
        print ('connecting to', remote_ip)
        s.connect((remote_ip, port))
        print ('connected')
        return s
    
    except (socket.error) as msg:
         print (' Failed' , + str(msg[0]), 'Message', + msg[1])

    except (excpet.gaierror):
        print ('host not found')
        sys.exit()
        
def send(s):

        try:
            while True:
                message = input('cin>> \n')
                message = str.encode(message)
                s.sendall(message)
                time.sleep(0.1)
        except (socket.error):
            print ('send failed')
            sys.exit()  
        finally:
            print ('closing socket')
##            s.close
            
def receive(s):
    while True:
        time.sleep(0.1)
        data = s.recv(16)
        print ('cout<< \n',data.decode())

def ComputeKey(s):

    # Recieve info server (Base, Mod, and Server public key)
    Key = s.recv(16)
    Key = Key.decode()
    Base, Mod, RKey = Key.split()
    Number = 5
    Base, Mod, RKey = int(Base), int(Mod), int(RKey)

    #Compute local public key
    PublicKey = str(Base**Number%Mod)

    #Send Local public key to server
    message = str.encode(PublicKey)
    s.sendall(message)

    #Compute private key
    SecretKey = RKey**Number%Mod
    print(SecretKey)
    return(SecretKey)

try:
    s = create_client()
    K = ComputeKey(s)
    threading._start_new_thread( receive,(s,))
    threading._start_new_thread( send, (s,))
    while True:
        time.sleep(0.1)
except:
    print('exception')


