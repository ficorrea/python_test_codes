""" Consulta modelo versão js """

import urllib3, requests, json
import sys
import random

# Variáveis de acesso
INSTANCE_ID = '4dc9cbe9-0160-4b3c-91cb-450387605b52'
APIKEY = '8uCS7iFWdfm-Ft3WpZWXn7AeY52UCRjYNiWH173hSpCV'
MODELO = 'https://us-south.ml.cloud.ibm.com/v4/deployments/e652076d-738a-4784-980e-d48d24549ce9/predictions'

def get_mltoken(apikey):
	"""Gera e retorna o token."""
	try:
		url = 'https://iam.bluemix.net/oidc/token'
		headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
		data = 'apikey=' + apikey + '&grant_type=urn:ibm:params:oauth:grant-type:apikey'
		IBM_cloud_IAM_uid = 'bx'
		IBM_cloud_IAM_pwd = 'bx'
		response  = requests.post(url, headers=headers, data=data, auth=(IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd))
		iam_token = response.json()['access_token']
		return iam_token
	except Exception as error:
		print('Erro na geração do token: {}'.format(error))
		end_script()

def cria_header(instance_id, apikey):
	"""Cria e retorna o header."""
	try:
		header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + get_mltoken(apikey), 'ML-Instance-ID': instance_id}
		return header
	except Exception as error:
		print('Erro na criação do header: {}'.format(error))
		end_script()

def response_post(link, payload, header):
	"""Executa a consulta do payload no Watson ML e por default deve retornar o resultado fornecido por ele."""
	try:
		response_scoring = requests.post(link, json=payload, headers=header)
		print('Response: {}\n'.format(json.loads(response_scoring.text)))
	except Exception as error:
		print('Erro no POST: {}'.format(error))
		end_script()

def consulta_modelo(modelo, payload, header):
	"""Recebe os dados, executa a consulta dos modelos e exbide o resultado.""" 
	response_post(modelo, payload, header)

def gera_payload(campos):
	array_decimal = [random.random() for i in range(campos - 1)]
	array_inteiro = [random.randint(1, 100)]
	payload = {"input_data": [{"fields": ["length", "diameter", "height", "whole_h", "shucked_w", "viscera_w", "shell_w", "rings"], "values": [array_decimal + array_inteiro]}]}
	return payload
		
def end_script():
	"""Finaliza execução do script."""
	return sys.exit()
		
if __name__ == "__main__":
	payload = gera_payload(8)
	header = cria_header(INSTANCE_ID, APIKEY)
	consulta_modelo(MODELO, payload, header)