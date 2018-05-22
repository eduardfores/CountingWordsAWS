# Eduard Fores Ferrer, Denys Sydorenko Sydorenko
# 17/05/2018 v1.0

from __future__ import print_function

import boto3
import json
import botocore
import re
import pickle

print('Loading function')

''' Definicion de variables globales. '''
ACCESS_KEY=''
SECRET_KEY=''
BUCKET_NAME=''

''' Comprobaciones para asegurarnos de que entramos en nuestro S3. '''
''' Diferencia entre resource y client, es que uno es de mas alto nivel que el otro. '''
s3 = boto3.resource('s3')
s3_b =boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

''' Definimos la funcion lambda_handles. '''
def lambda_handler(event, context):
    ''' Leemos los parametros introducidos que son el nombre del fichero y el numero de mappers. '''
    obj = s3.Object(BUCKET_NAME,event['key1'])
    num = event['key2']
    
    ''' Obtenemos la secuencia y le quitamos los caracteres basura. '''
    sequence1 = re.sub('[^ a-zA-Z0-9]', ' ', obj.get()['Body'].read())

    ''' Tratamos el map_list. '''
    map_list={}
    for word in sequence1.split():
        word=word.encode('utf-8')
        if word not in map_list:
            map_list[word] = 1
        else:
            map_list[word] += 1

    ''' Escribimos la variable map_list en el fichero save.txt con pickle.dump(). '''
    pickle.dump(map_list, open( "/tmp/save.txt", "wb"))

    ''' Subimos el fichero que hemos escrito al nuestro BUCKET. '''
    s3_b.upload_file("/tmp/save.txt", BUCKET_NAME, "save"+str(num)+".txt")