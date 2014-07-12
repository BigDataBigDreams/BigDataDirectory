import csv
import MySQLdb

db = MySQLdb.connect('localhost','govhack', 'gov', 'govhack')
cur = db.cursor()

#fout = open('c:\\wamp\\www\\data\\dump.txt', 'w')
def ex(sql):
	#fout.write(sql+"\n")
	cur.execute(sql)

class DataSet:
	def __init__(self, name, pref, keys):
		self.name = name
		self.keys = keys
		self.pref = pref
		
	def createString(self):
		try:
			ex("drop table %s;"%self.name)
		except Exception as e:
			print "Couldn't drop %s"%self.name
		s = """create table %(name)s (
		%(pref)s_id mediumint not null auto_increment,
		%(pref)s_brand varchar(64),
		%(pref)s_model varchar(128),
		%(pref)s_power decimal(6,3),
		%(pref)s_star decimal(2,1),
		PRIMARY KEY (%(pref)s_id));"""
		return s.replace('\\w+', ' ') %({'name':self.name,'pref':self.pref})
		
	def colArray(self):
		cols = {}
		indexs = {}
		with open(r'C:\wamp\www\data\%s.csv'%self.pref, 'r') as fin:
			reader = csv.reader(fin)
			headers = reader.next()
			for dbKey in self.keys:
				cols[dbKey] = []
				indexs[dbKey] = headers.index(self.keys[dbKey])
			for row in reader:
				for dbKey in self.keys:
					cols[dbKey].append(row[indexs[dbKey]])
		return cols
		
	def createTable(self):
		ex(self.createString())
	
	def formatVal(self, key, val):
		if key in ["brand","model"]:
			return "'%s'"%val
		return val
	
	def insert(self):
		s = ""
		cols = self.colArray()
		length = len(cols['model'])
		for j in xrange(0, length):
			order = []
			for key in self.keys:
				if cols[key][j] != "":
					order.append(key)
			sql = "insert into %s (%s_"%(self.name,self.pref)
			sql += (",%s_"%self.pref).join(order)
			sql += ") values ("
			sql += ",".join([self.formatVal(k, cols[k][j]) for k in order])
			sql += ");"
			ex(sql)
			

keys = {'brand':'Brand','model':'Model_No','star':'Star2010_Heat','power':'H-Power_Inp_Rated'}
dset = DataSet('airconditioner', 'ac', keys)	

dset.createTable()
dset.insert()
#fout.close()
#with open('c:\\wamp\\www\\data\\dump.txt', 'w') as fout:
#	fout.write(dset.createString())
