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
PATH='/tmp/'

s3_b =boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def lambda_handler(event, context):
    map_final={}
    respuesta=dict()
    num=event['Key1']
    count=0
    
    for i in range(0,num):
        s3_b.download_file(BUCKET_NAME, "save"+str(i)+".txt", PATH+"save"+str(i)+".txt")
        aux = pickle.load( open( PATH+"save"+str(i)+".txt", "rb" ) )
        aux=dict(aux)
        
        if len(map_final)==0:
                map_final=aux
                for j in aux.keys():
                    count=count+aux.get(j)
        else:
            for k in aux.keys():
                if map_final.has_key(k):
                    map_final[k]=map_final.get(k)+aux.get(k)
                else:
                    map_final[k]=m.get(k)
                count=count+aux.get(k)
    respuesta['map']=map_final
    respuesta['counting']=count
    
    pickle.dump( respuesta,open( "/tmp/save_final.txt", "wb" ))
    s3_b.upload_file("/tmp/save_final.txt", BUCKET_NAME, "save_final.txt")
    return respuesta