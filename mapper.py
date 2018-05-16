from __future__ import print_function

import boto3
import json
import botocore
import re
import pickle

print('Loading function')

ACCESS_KEY='AKIAIOIOCNMRWM34L5ZQ'
SECRET_KEY='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'
BUCKET_NAME='putamierdadedocumentaciones'

s3 = boto3.resource('s3')
s3_b =boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

'''
s3=boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
'''
    
def lambda_handler(event, context):
    obj = s3.Object(BUCKET_NAME,event['key1'])
    num= event['key2']
    
    #sequence=obj.get()['Body'].read()
    sequence1 = re.sub('[^ a-zA-Z0-9]', ' ', obj.get()['Body'].read())
    #Countingwords countwords=len(sequence1.split())
    map_list={}
    for word in sequence1.split():
        word=word.encode('utf-8')
        if word not in map_list:
            map_list[word] = 1
        else:
            map_list[word] += 1
    pickle.dump( map_list,open( "/tmp/save.txt", "wb" ))
    s3_b.upload_file("/tmp/save.txt", BUCKET_NAME, "save"+str(num)+".txt")