#from concurrent.futures import ThreadPoolExecutor

import boto3
import botocore
import sys
import json
import os
import time

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

txt=""

os.system("mkdir -p "+PATH)

"maxim 6291456"
payload3=dict()
payload3["key1"]=FILE

s3=boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3_r=boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

#Subida
#s3.upload_file(FILE, BUCKET_NAME, FILE)
#Descarga
'''
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

client = boto3.client('lambda', region_name="eu-west-3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

for i in range(0,n):
	payload3["key2"]=i
	client.invoke(
		FunctionName="mapper",
		InvocationType='Event',
		Payload=json.dumps(payload3)
	)

time.sleep(20)

payload3={
	"Key1":n
}

response=client.invoke(
	FunctionName="reducer",
	InvocationType='RequestResponse',
	Payload=json.dumps(payload3)
)
print response['Payload'].read()


