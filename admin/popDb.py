import csv
import MySQLdb

db = MySQLdb.connect('localhost','govhack', 'gov', 'govhack')
cur = db.cursor()

def ex(sql):
	cur.execute(sql)

class DataSet:
	def __init__(self, name, pref, keys):
		self.name = name
		self.keys = keys
		self.pref = pref
		
	def createString(self):
		s = """create table %(name)s (
		%(pref)s_id mediumint not null auto_increment,
		%(pref)s_brand varchar(32),
		%(pref)s_model varchar(32),
		%(pref)s_power decimal(4,2),
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
	
	def formatVal(key, val):
		if key in ["brand","model"]:
			return '"'+val+'"'
		return val
	
	def insert(self):
		s = ""
		cols = self.colArray()
		length = len(cols['model'])
		ind = 0
		for j in xrange(0, length):
			order = []
			for key in self.keys:
				if cols[key][order] != "":
					order.append(key)
			sql = "insert into (" + ",".join(order)") values ("
			sql += ",".join([formatRow(key, cols[key][j]) for k in order])
			sql += ");"
			ex(sql)
			ind += 1
			print ind
			

keys = {'brand':'Brand','model':'Model_No','star':'Star2010_Heat','power':'H-Power_Inp_Rated'}
dset = DataSet('airconditioner', 'ac', keys)	

try:
	dset.createTable()
	dset.insert()
except Exception as e:
	print "uh oh "
	print e

#with open('c:\\wamp\\www\\data\\dump.txt', 'w') as fout:
#	fout.write(dset.createString())
