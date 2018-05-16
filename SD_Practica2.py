# Eduard Fores Ferrer, Denys Sydorenko
# 17/05/2018 v1.0

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

''' Si el segundo parametro introducido es superior a 5, entonces se muestra el mensaje de error. '''
if n > 5:
	print "\nNo pueden haber mas de 5 mappers.\n"
	sys.exit(0)

''' Si el segundo parametro introducido es inferior a 1, entonces se muestra el mensaje de error. '''
if n < 1:
	print "\nNo pueden haber menos de 1 mappers.\n"
	sys.exit(0)

''' Creamos el Path en el que haremos funcionar nuestro programa. '''
os.system("mkdir -p "+PATH)

''' Ponemos el nombre del fichero en el key1. '''
payload3=dict()
payload3["key1"]=FILE

''' Definiciones de ACCESS_KEY y SECRET_KEY para poder acceder desde fuera de Amazon. '''
''' Diferencia entre resource y client, es que uno es de mas alto nivel que el otro. '''
s3=boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3_r=boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

''' Para subir un archivo a nuestro BUCKET de Amazon. '''
#s3.upload_file(FILE, BUCKET_NAME, FILE)

''' Para descargar un archivo de nuestro BUCKET de Amazon. '''
'''
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
'''

''' Definiciones de ACCESS_KEY y SECRET_KEY para poder acceder desde fuera de Amazon. '''
client = boto3.client('lambda', region_name="eu-west-3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

''' Invocamos a los mappers. '''
for i in range(0,n):
	''' Cada mapper tendra el fichero que tiene que leer y el identificador de mapper. '''
	payload3["key2"]=i
	client.invoke(
		FunctionName="mapper",
		InvocationType='Event',
		Payload=json.dumps(payload3)
	)

''' Ponemos el sleep de 20 segundos porque los mapper tardan unos 15 segundos mas o menos. '''
time.sleep(20)

''' Definimos el payload3 que utilizaremos a continuacion. '''
payload3={
	"key1":n
}

''' Invocamos al reducer. '''
response=client.invoke(
	FunctionName="reducer",
	InvocationType='RequestResponse',
	Payload=json.dumps(payload3)
)

''' Devuelve por pantalla el map_final y el numero total de palabras. '''
print response['Payload'].read()


