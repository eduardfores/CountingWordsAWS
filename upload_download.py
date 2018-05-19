# Eduard Fores Ferrer, Denys Sydorenko
# 17/05/2018 v1.0

#Comentario
#Introducimos el nombre del fichero y seguidamente un numero, si el numero es 1 entonces
#subimos el fichero a nuestro BUCKET, sino descargaremos el fichero de nuestro BUCKET.

#from concurrent.futures import ThreadPoolExecutor

import boto3
import botocore
import sys
import json
import os
import time

''' Definicion de variables globales. '''
ACCESS_KEY='AKIAIOIOCNMRWM34L5ZQ'
SECRET_KEY='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'
BUCKET_NAME='putamierdadedocumentaciones'
PATH='/home/milax/Desktop/SD_AWS/'
FILE=sys.argv[1]
n=int(sys.argv[2])

''' Creamos el Path en el que haremos funcionar nuestro programa. '''
os.system("mkdir -p "+PATH)

''' Ponemos el nombre del fichero en el key1. '''
payload3=dict()
payload3["key1"]=FILE

''' Definiciones de ACCESS_KEY y SECRET_KEY para poder acceder desde fuera de Amazon. '''
s3=boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

''' Para subir un archivo a nuestro BUCKET de Amazon. '''
if(n == 1):
	s3.upload_file(FILE, BUCKET_NAME, FILE)

''' Para descargar un archivo de nuestro BUCKET de Amazon. '''
else:
	txt=""
	try:
		s3.download_file(BUCKET_NAME, FILE, PATH+FILE)
	except botocore.exceptions.ClientError as e:
		if e.response['Error']['Code']=="404":
			print("The object does not exist.")
		else:
			raise

	with open(PATH+FILE, 'r') as reader:
		for line in reader:
			txt+=line
	payload3["key1"]=txt