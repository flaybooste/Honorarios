import json
import leitorcsv

def escreverJson():
	with open('./static/db.json', 'w') as _f:
		try:
			json.dump(leitorcsv.ler(), _f)
		except:
			#print('nao funcionou')
			pass