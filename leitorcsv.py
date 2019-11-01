import csv
import re

d = {}
d0 = []
def ler():
	with open('completa.csv') as _f:
		linhas = csv.reader(_f)
		x = 0
		for linha in linhas:
			if(linha[0] != "" and linha[0] != 'Relatório Completo de Empresas'):
				news = linha[0].replace('(',',').replace(')', ',')
				d0.append(news.split(','))
				'''
				for k in linha[0]:
					if(k != "(" and k != ")" and k!= "0" and k!= ""):
						print(k)
						#n1 = "".join(n)
						#print(n1)
					#d0.append(n1)
				'''
				print(d0)
				d[x] = linha[0]
				x+=1
		#print(d)
		#return d
				