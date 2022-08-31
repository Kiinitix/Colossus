"""

This python file is a part of an open-source
project Colossus (https://github.com/Kiinitix/Colossus).

Implementation of Hybrid Cryptography (AES + RSA)

Required fields -> file location for encrypting the content of the text file

"""

import euclid
import mail
from configparser import ConfigParser
import secrets
from Cryptodome.Cipher import AES
from Cryptodome import Random
import stego

def mainMenu():
    print("\n******************************************************************")
    print("******************************************************************")
    print("Welcome...")
    print("We're going to encrypt and decrypt a message using AES and RSA")
    print("******************************************************************")
    print("******************************************************************\n")

    #configur = ConfigParser()
    #configur.read('configurations.ini')
    #location = configur.get('SMTPlogin', 'file_location')

    # Obtains public key.
    print("Genering RSA public and Privite keys......")
    pub,pri=euclid.KeyGeneration()

    # Generates a fresh symmetric key for the data encapsulation scheme.
    print("Genering AES symmetric key......")
    key = secrets.token_hex(16)
    KeyAES=key.encode('utf-8')

    # Encrypts the message under the data encapsulation scheme, using the symmetric key just generated.
    plainText = input("Enter the message: ")
    cipherAESe = AES.new(KeyAES,AES.MODE_GCM)
    nonce = cipherAESe.nonce

    print("Encrypting the message with AES......")
    cipherText=euclid.encryptAES(cipherAESe,plainText)
    src = input(r"Enter image source: ")
    stego.Encode(src, cipherText, src)

    print("Successfully encrypted and hidden the text in picture......")

    # Encrypt the symmetric key under the key encapsulation scheme, using Alice’s public key.
    cipherKey=euclid.encrypt(pub,key)
    print("Encrypting the AES symmetric key with RSA......")

    # sending mail
    mail.mail(pri, cipherKey, nonce, src)
