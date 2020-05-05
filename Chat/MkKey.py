from cryptography.fernet import Fernet

def write_key():

    key = Fernet.generate_key()
    
    with open("key.key","w") as key_file:
        key_file.write(key)


def load_key():
    
    return open("key.key","r").read()
