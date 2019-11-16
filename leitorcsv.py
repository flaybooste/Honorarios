import csv
from db import dbSQL
from pprint import pprint
import pdb

def inserirSQL():
	with open('completa.CSV',encoding='ISO-8859-1') as _f:
		linhas = csv.reader(_f)
		x = 0
		d0 = []
		for linha in linhas:
                    #pdb.set_trace()
                    print(linha[0].strip())
                    #if(linha[4] != ""):
                    #       pprint(linha[4])
                    if(linha[0] != "" and linha[0] != 'Relatório Completo de Empresas'):
                        try:	
                            news = linha[0].replace('(',',').replace(')', ',')
                            d0.append(news.split(','))
                            #dbSQL().escreverSQL(d0[x][1], d0[x][0])
                    #        print(d0[x][1] in d1)
                            x+=1
                        except:
                            pass
		#print(d1.values())
	#return d2
