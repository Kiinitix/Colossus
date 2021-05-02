import secrets
import random
import sys
from Crypto.Cipher import AES
from Crypto import Random 
import hybrid

pri=input("Enter the Private Key: ")
cipherKey=input("Enter the AES Symmetric Key: ")
cipherText=input("Enter cipher text: ")

decriptedKey=''.join(decrypt(pri,cipherKey))
print()
print("Decrypting the AES Symmetric Key...")

decriptedKey=decriptedKey.encode('utf-8')
cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
decrypted=decryptAES(cipherAESd,cipherText)
print()
print("Decrypting the message using the AES symmetric key.....")
print("decrypted message: ", decrypted)
