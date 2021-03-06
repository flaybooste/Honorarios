import json
#import leitorcsv
import sqlite3

class dbSQL:
	def __init__(self):
		self.con = sqlite3.connect('./static/main.db')
		self.cur = self.con.cursor()

	def criarSQL(self):
		self.cur.execute('''CREATE TABLE empresas(
			id INTEGER PRIMARY KEY,
			nome TEXT NOT NULL
		);
		''')

	def escreverSQL(self, id, nome):
		try:
			print(id, nome)
			self.cur.execute("INSERT INTO empresas VALUES({}, '{}')".format(id, nome))
			self.con.commit()
			print("com sucesso")
		except:
			print('sem sucesso')
			pass

	def selectSQL(self):
		sq = self.cur.execute('SELECT * FROM empresas ORDER BY id')
		return sq.fetchall()

	def alterarTbl(self):
		self.cur.execute("ALTER TABLE empresas ADD COLUMN valor")

	def selectId(self, id):
		return self.cur.execute('SELECT * FROM empresas WHERE id={}'.format(id)).fetchall()

	def updateTblValor(self, valor, id):
		self.cur.execute('UPDATE empresas SET valor={} WHERE id={}'.format(valor, id))
		self.con.commit()

	def updateAllTblValor(self, valor):
		self.cur.execute('UPDATE empresas SET valor={}'.format(valor))
		self.con.commit()
