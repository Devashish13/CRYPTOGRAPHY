#caeser Cipher
import pyperclip

#the string to be encrypted/decrypted
message=input('enter the message to be encrypted/decrypted:')

#encryption/decryption key
key=int(input('enter the key:'))

#encryption/decryption mode
mode=input("enter (encrypt) for encryption or (decrypt) for decryption:") #set to encrypt or decrypt

#every possible symbol that can be encrypted
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#stores the encrypted or decrypted form of message
translated=''

#capitalise the message

message=message.upper()


#run encryption/decryption code on each symbol in message string

for symbol in message:
    if symbol in LETTERS:
        num=LETTERS.find(symbol)#give sorresponding number of symbol in LETTERS
        if mode=='encrypt':
            num=num+key
        elif mode=='decrypt':
            num=num-key
        if num>=len(LETTERS):
            num=num-len(LETTERS)
        elif num<0:
            num=num+len(LETTERS)

        translated=translated+LETTERS[num]

    else:
        translated=translated+symbol
print(translated)

pyperclip.copy(translated)

            

