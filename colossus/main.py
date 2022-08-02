"""
This python file is a part of an open-source
project Colossus (https://github.com/Kiinitix/Colossus).

"""
import getopt, sys
import hybrid
import uploadS3
import os
import boto3
import decrypt

def main():
    bucket = None
    object = None
    src = None
    type = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "b:o:i:t:h:")

    except:
        print ("usage: python3 main.py -t upload -b <bucket-name> -o <object> -i <image-name>")
        print ("usage: python3 main.py -t download -b <bucket-name> -o <object> -i <image-name>")
        print("usage: python3 main.py -t decrypt -i <image-name>")
        sys.exit(2)

    else:
        for opt, arg in opts:
            if opt in ['-h']:
                print ("usage: python3 main.py -t upload -b <bucket-name> -o <object> -i <image-name>")
                print ("usage: python3 main.py -t download -b <bucket-name> -o <object> -i <image-name>")
                print ("usage: python3 main.py -t decrypt -i <image-name>")
                os._exit(0)

            elif opt in ['-t']:
                type = arg
            elif opt in ['-b']:
                bucket = arg
            elif opt in ['-o']:
                object = arg
            elif opt in ['-i']:
                src = arg
        if (type == "upload"):
            hybrid.mainMenu()
            uploadS3.upload_file(src, bucket, object)
            print("Uploaded Successfully!!!")

        elif (type == "download"):
            s3 = boto3.client('s3')
            s3.download_file(bucket, object, src)
            print("File Downloaded!!!")

        elif (type == "decrypt"):
            decrypt.main(src)

if __name__ == '__main__':
    main()

# Test
# python main.py -t upload -b sefy0 -i Capture1.PNG
# python main.py -t download -b sefy0 -o Capture1.PNG -i Capture1.PNG
