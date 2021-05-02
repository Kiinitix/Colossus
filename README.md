## Sefy  ##

Objective: To make secure file storage in cloud computing using hybrid cryptography.

In today’s world 99% people are more interested in sending and receiving data through internet and mobile data storage devices. But among those people don’t encrypt their data though they know that data contains personal information and the chances of data lose or hacking is very high. Information security has always been important in all aspects of life. It can be all the more important as technology continues to control various operations in our day-to-day life. Cryptography provides a layer of security in cases, where the medium of transmission is susceptible to interception, by translating a message into a form that cannot be read by an unauthorized third part.The ultimate objective of the program is to develop both AES and RSA to be low power, high-throughput, real-time, reliable and extremely secure cryptography algorithm.

Security breaches are rarely caused by poor cloud data protection. More than 40% of data security breaches occur due to employee error. Improve user security to make storage more secure.Cloud-based internet security is an outsourced solution for storing data. Instead of saving data onto local hard drives, user store data on Internet-connected servers. Data Centers manage these servers to keep the data safe and secure to access.
Cloud-based solutions are increasingly in demand around the world. These solutions include everything from secure data storage to entire business processes.

# Features
* Secure file data in AWS Cloud.
* Key is sent directly to you email ID.
* Pure-Python
* Decryption software is with the end users only.

# To Do
- [ ] Using steganography to hide the key in image and mailing that image insted of simple text mail.
- [ ] Using more than two encryption algorithm to make the file even more secure.
- [ ] Login function for end users

# Hybrid Cryptography

Hybrid encryption is a mode of encryption that merges two or more encryption systems. It incorporates a combination of asymmetric and symmetric encryption to benefit from the strengths of each form of encryption. These strengths are respectively defined as speed and security.

Hybrid encryption is considered a highly secure type of encryption as long as the public and private keys are fully secure.

A hybrid encryption scheme is one that blends the convenience of an asymmetric encryption scheme with the effectiveness of a symmetric encryption scheme.

Hybrid encryption is achieved through data transfer using unique session keys along with symmetrical encryption. Public key encryption is implemented for random symmetric key encryption. The recipient then uses the public key encryption method to decrypt the symmetric key. Once the symmetric key is recovered, it is then used to decrypt the message.

The combination of encryption methods has various advantages. One is that a connection channel is established between two users' sets of equipment. Users then have the ability to communicate through hybrid encryption. Asymmetric encryption can slow down the encryption process, but with the simultaneous use of symmetric encryption, both forms of encryption are enhanced. The result is the added security of the transmittal process along with overall improved system performance.


The idea of hybrid encryption is quite simple. Instead of using AES to encrypt the text, we use AES to encrypt the message. Then, they maintain the secrecy of the key, and we encrypt the key using RSA. The steps of hybrid encryption are:


    1. Generate a symmetric key. The symmetric key needs to be kept a secret.
    2. Encrypt the data using the secret symmetric key.
    3. The person to whom we wish to send a message will share her public key and keep the private key a secret.
    4. Encrypt the symmetric key using the public key of the receiver.
    5. Send the encrypted symmetric key to the receiver.
    6. Send the encrypted message text.
    7. The receiver decrypts the encrypted symmetric key using her private key and gets the symmetric key needed for decryption.
    8. The receiver uses the decrypted symmetric key to decrypt the message, getting the original message.


# Why to use Python for Cryptography?

Python makes implementing certain types of algorithms easy without being insanely slow, namely those that use a few simple operations on BigIntegers (RSA, DH, etc).
Symmetric algorithms such as AES or SHA256 implemented in Python will be slow.
For writing simple programs to cryptanalyze classic ciphers, Python is a pretty solid choice - normally they are weak enough to not require huge amounts of CPU time to crack.  Python has a relative small quantity of lines of code, which makes it less prone to issues, easier to debug, and more maintainable.

![Screenshot (1583)](https://user-images.githubusercontent.com/34811605/116817461-161d8c00-ab84-11eb-8a93-fb9a48c05477.png)

![Screenshot (1585)](https://user-images.githubusercontent.com/34811605/116817465-1c136d00-ab84-11eb-82ff-28e06a672515.png)
