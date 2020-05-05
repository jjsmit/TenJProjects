import socket
import sys
import threading
import time


def create_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ('socket created')
        host = '84.80.93.149'
        port = 8001
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
                message = input('write message')
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
        print ('received', data.decode())

try:
    s = create_client()
    threading._start_new_thread( receive,(s,))
    threading._start_new_thread( send, (s,))
    while True:
        time.sleep(0.1)
except:
    print('exception')


