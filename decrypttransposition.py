import math
import pyperclip
def decryptMessage(message,key):
    ncol=math.ceil(len(message)/key)
    nrows=key
    nshadedbox=(ncol*nrows)-len(message)

    plaintext=['']*ncol
    col=0
    row=0
    for symbol in message:
        plaintext[col]+=symbol
        col+=1

        if (col==ncol) or (col==(ncol-1) and row>=(nrows-nshadedbox)):
            col=0
            row=row+1
            
    return ''.join(plaintext)

Mymessage=input('enter your message:')
key=int(input('enter your key:'))

plaintext=decryptMessage(Mymessage,key)
print(plaintext+'|')
pyperclip.copy(plaintext)
