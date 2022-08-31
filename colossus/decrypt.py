"""

This python file is a part of an open-source
project Colossus (https://github.com/Kiinitix/Colossus).

This file is made for the end user to be used for
decryption process as part of hybrid-cryptography
implementation used in Colossus.

"""

import secrets
import random
import sys
from Cryptodome.Cipher import AES
from Cryptodome import Random
#import hybrid
import stego
import numpy as np
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)

def decryptAES(cipherAESd,cipherText):
    dec= cipherAESd.decrypt(cipherText)
    return dec

def decrypt(pk, ciphertext):
    d, n = pk
    m = [chr((char ** d) % n) for char in ciphertext]
    return m

def Decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        #return message[:-5]
        print("Hidden Message:", message[:-5])
    else:
        print("No Hidden Message Found")

def main(src):
    #cipherText = bytes(Decode(src), 'utf-8')
    Decode(src)
    pri = tuple(int(item) for item in input("Enter the Private Key: ").split(','))
    cipherKey=[int(item) for item in input("Enter the AES Symmetric Key: ").split(',')]
    #cipherText= input("Enter cipher text: ")
    cipherText = b'\x00.\xfbZu\xc9\xda@-'
    nonce= b'\xf9\x7fo\xb1g\xf5I\xcd\xd5\x89\xb3D\xc3\xd4:\x95'

    decriptedKey = ''.join(decrypt(pri,cipherKey))
    print("Decrypting the AES Symmetric Key...")

    decriptedKey = decriptedKey.encode('utf-8')
    cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
    decrypted = decryptAES(cipherAESd,cipherText)
    print("\nDecrypting the message using the AES symmetric key.....")
    print("Decrypted message: ", decrypted)
