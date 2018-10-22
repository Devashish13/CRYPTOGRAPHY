import pyperclip

def encryptMessage(message,key):
    #each string in cyphertext represents a coloumn   
    ciphertext=['']*key

    #loop through each column in cypher text 
    for col in range(key):
        pointer=col
        #keep looping until pointer goes past length of message
        while pointer<len(message):
            
            ciphertext[col]+=message[pointer]
            #move pointer to current column of next row
            pointer+=key

    return ''.join(ciphertext)

message=input('enter your message:')

key=int(input('enter the key:'))

ciphertext=encryptMessage(message,key)
pyperclip.copy(ciphertext)
print(ciphertext+'|')


        
