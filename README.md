## Colossus  ##

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
- [ ] Not only encrypting the content of the file but also encrypting the whole format of the file itself.
- [ ] Login function for end users

# Getting Started

To get started with the code on this repo, you need to either clone or download this repo into your machine just as shown below;

```
git clone https://github.com/Kiinitix/Colossus
cd Colossus
```

# Dependencies

Before you begin playing with the source code you might need to install deps just as shown below;

`pip3 install -r requirement.txt`

# Setting up AWS S3

For setting up AWS S3 for uploading and featching files from the bucket you first need to setup your AWS account and create a bucket.
To do so, you can follow the following documentation of [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

You probably want to setup IAM users and give the access either though a bucket policy or on the user level. With bucket policies you can easily define what paths users are able to edit and access. When you create an IAM user you also have the option of creating one for Programmatic(CLI) access only which will give you a set of credentials for that user only. Just use aws configure and set the access and token key.

You also probably want to make sure you are using an IAM user yourself as it's generally recommended for security.

To do so, you can go here [AWS Access Key](https://console.aws.amazon.com/iam/home#/security_credentials$access_key) and under the Access keys (access key ID and secret access key) section click on 'Create New Access Key'. And don't forget to note down the AWS Secret Access Key because it is kinda one time thing and if you lose or forget your secret key, you cannot retrieve it. Instead, you have to create a new access key and make the old key inactive.

After noting down the credentials, open the windows cmd and type

`aws configure`

Enter the AWS Access Key ID and AWS Secret Access Key. Now you are good to go!

# Setting up Mailtrap account

The decryption phase of this process involves the use of your Mailtrap account.
You need to sign up for [Mailtrap account.](https://mailtrap.io) After signing up you just need to keep the Mailtrap username and Mailtrap password handy to use their API.

Now, naviagate to **Colossus/generate_config.py** and edit the required parameters. You can find the smtp login details [here,](https://mailtrap.io/inboxes) under the **SMPT settings** option. 
After editing, run this python script, it will generate a **configurations.ini** in the same directory which will be used to easily configure the software for you.

 `python generate_config.py`
 
# Running the App
In order to run the app on your device run this command,

`python main.py -h`

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

# Output

![Screenshot (346)](https://user-images.githubusercontent.com/34811605/182296556-4e0a5e05-b099-46a8-8349-b7eee842ed09.png)

![Screenshot (318)](https://user-images.githubusercontent.com/34811605/182296664-3ff35630-8f74-4952-8ad3-c3018205e8d9.png)

![Screenshot (319)](https://user-images.githubusercontent.com/34811605/182296719-e079a955-4597-4711-9ee6-5e01b0e03206.png)


# Email

![Screenshot (345)](https://user-images.githubusercontent.com/34811605/182295482-372be1e6-e52a-4e90-9f9f-d9019b107e64.png)


# Core Operation

![Screenshot (1904)](https://user-images.githubusercontent.com/34811605/122540457-4a6ede00-d046-11eb-966d-57cad61d7e99.png)

# Explore it!

Explore it and twist it to your own use case, in case of any question feel free to reach me out directly `kabirdhruw24@gmail.com`.

# Some Facts about the Colossus

Colossus was the world’s first electronic, programmable computer created by Tommy Flowers. It was used by the British to read secret German messages (encrypted by the Lorenz cipher) during World War II.

The Colossus was not supposed to decrypt all of a message. It just found close settings for the Lorenz machines. The idea was that the frequencies of letters and numerals in German message would give a start to translating the message itself.

Until the 1970s, these computers were very secret. After the war, all Colossus were broken into bits and designs were destroyed. No one knew the first people to make Colossus. In 2007, engineers made a working prototype of Colossus.
