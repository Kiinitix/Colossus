import getopt, sys
import hybrid
import uploadS3
import os
import boto3

def main():
    bucket = None
    object = None
    file = None
    type = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "b:o:f:t:h:")

    except:
        print ("usage: python3 main.py upload -b <bucket-name> -o <object> -f <file-name>")
        print ("usege: python3 main.py download -b <bucket-name> -o <object> -f <file-name>")
        sys.exit(2)

    else:
        for opt, arg in opts:
            if opt in ['-h']:
                print ("usage: python3 main.py upload -b <bucket-name> -o <object> -f <file-name>")
                print ("usege: python3 main.py download -b <bucket-name> -o <object> -f <file-name>")
                os._exit(0)
            elif opt in ['-t']:
                type = arg
            elif opt in ['-b']:
                bucket = arg
            elif opt in ['-o']:
                object = arg
            elif opt in ['-f']:
                file = arg

        if (type == "upload"):
            hybrid.mainMenu()
            uploadS3.upload_file(file, bucket, object)
            print("Uploaded Successfully!!!")

        elif (type == "download"):
            s3 = boto3.client('s3')
            s3.download_file(bucket, object, file)
            print("File Downloaded!!!")

if __name__ == '__main__':
    main()

# Test
# python main.py -t upload -b sefy0 -o test.txt -f test.txt
