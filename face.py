#!/usr/local/bin/python3

import boto3
import os
import json
import argparse

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

# command line arguments
parser = argparse.ArgumentParser(description='Run face recognition from image file with Amazon Rekognition')
parser.add_argument('image', help='Souece image name')
parser.add_argument('region', default='us-east-1', nargs='?', help='Comprehend region (default=us-east-1')
args = parser.parse_args()
print(args)

if __name__ == "__main__":

    fileName=args.image
    threshold = 50
    maxFaces=1

    client=boto3.client('rekognition')
    os.system('open -a Preview %s' % fileName)

    imageSource=open(fileName,'rb')

    response=client.detect_protective_equipment(
                                Image={'Bytes': imageSource.read()},
                                )

    print (json.dumps(response, sort_keys=True, indent=4))
