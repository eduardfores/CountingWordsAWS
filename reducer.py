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
PATH='/tmp/'

''' Comprobaciones para asegurarnos de que entramos en nuestro S3. '''
s3_b =boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

''' Definimos la funcion lambda_handles. '''
def lambda_handler(event, context):
    map_final={}
    respuesta=dict()
    num=event['key1']
    count=0
    
    for i in range(0,num):
        ''' Descargamos los ficheros de nuestro BUCKET. '''
        s3_b.download_file(BUCKET_NAME, "save"+str(i)+".txt", PATH+"save"+str(i)+".txt")
        ''' Utilitzamos pickle.load() para obtener lo que hemos guardado en el fichero. '''
        aux = pickle.load( open( PATH+"save"+str(i)+".txt", "rb" ) )
        ''' Passamos lo obtenido en el paso anterior al formato de diccionario. '''
        aux=dict(aux)
        
        ''' Si el map_final es vacio se hace la primera iteracion para tener el Map entero de los X mappers y las palabras totales de este Map. '''
        if len(map_final)==0:
            map_final=aux
            for j in aux.keys():
                count=count+aux.get(j)
        ''' Si no, concatenamos los Maps de los siguientes mappers al map_final y sumas el contador de palabras. '''
        else:
            for k in aux.keys():
                if map_final.has_key(k):
                    map_final[k]=map_final.get(k)+aux.get(k)
                else:
                    map_final[k]=m.get(k)
                count=count+aux.get(k)

    ''' Guardamos el map_final y el numero total de palabras en una variable para escribirla en el fichero final. '''
    respuesta['map']=map_final
    respuesta['counting']=count

    ''' Escribimos la variable respuesta en el fichero save_final.txt con pickle.dump(). '''
    pickle.dump(respuesta, open( "/tmp/save_final.txt", "wb" ))

    ''' Subimos el fichero que hemos escrito al nuestro BUCKET. '''
    s3_b.upload_file("/tmp/save_final.txt", BUCKET_NAME, "save_final.txt")

    ''' Devolvemos por pantalla el WordCount y el CountingWords. '''
    return respuesta