import MkKey
from cryptography.fernet import Fernet


MkKey.write_key()

key = MkKey.load_key()

f = Fernet(key)

message = raw_input ("Enter message:")

encrypted = f.encrypt(message)

decrypted = f.decrypt(encrypted)

print "key is:" + key

print "encrypted message:" + encrypted

print "decypted message:" + decrypted 

