__author__ = 'mpetyx'

import json
import binascii
import datetime
import struct
import boto3
import string, random

s3 = boto3.client('s3')

from boto.s3.connection import S3Connection


    

def lambda_handler(event, context):
    conn = S3Connection('access-key', 'secret-access-key')
    bucket = conn.get_bucket('bucket')
    for key in bucket.list():
        print
        key.name.encode('utf-8')

    return {'status': 200, 'data': {}}