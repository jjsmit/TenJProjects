def encrypt(message):
    myInt = 3
    encMessage = ""
    for x in message:   
       encMessage += chr(ord(x)^myInt)

    return encMessage
    


message = "hello world"
encMessage= encrypt(message)
print(encMessage) 
print(encrypt(encMessage))



   

