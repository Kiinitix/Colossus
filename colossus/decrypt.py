import secrets
import random
import sys
from Crypto.Cipher import AES
from Crypto import Random 
import hybrid

def decryptAES(cipherAESd,cipherText):
    dec= cipherAESd.decrypt(cipherText)
    return dec

def decrypt(pk, ciphertext):
    d, n = pk
    m = [chr((char ** d) % n) for char in ciphertext]
    return m

pri = tuple(int(item) for item in input("Enter the Private Key: ").split(','))
cipherKey=[int(item) for item in input("Enter the AES Symmetric Key: ").split(',')]
cipherText= <cipher-text-from-the-file>
nonce= <included-in-email>

decriptedKey=''.join(decrypt(pri,cipherKey))
print("Decrypting the AES Symmetric Key...")

decriptedKey=decriptedKey.encode('utf-8')
cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
decrypted=decryptAES(cipherAESd,cipherText)
print("\nDecrypting the message using the AES symmetric key.....")
print("decrypted message: ", decrypted)
