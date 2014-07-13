import csv
import MySQLdb

db = MySQLdb.connect('localhost','govhack', 'gov', 'govhack')
cur = db.cursor()

fout = open('C:\\wamp\\www\\data\\dump.txt', 'w')
def ex(sql):
	try:
		print sql
		fout.write(sql+"\n")
		cur.execute(sql)
		while cur.nextset() is not None: pass
	except Exception as e:
		print e
		
class DataSet:
	def __init__(self, name, pref, keys):
		self.name = name
		self.keys = keys
		self.pref = pref
		
	def dropString(self):
		return "drop table if exists %s;"%self.name
	
	def createString(self):
		return """create table %(name)s (
		id mediumint not null auto_increment,
		brand varchar(64),
		model varchar(128),
		power decimal(6,3),
		star decimal(2,1),
		PRIMARY KEY (id));"""%({'name':self.name})
		
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
	
	def insertString(self):
		cols = self.colArray()
		length = len(cols['model'])
		for j in xrange(0, length):
			order = []
			for key in self.keys:
				if cols[key][j] != "":
					order.append(key)
			sql = "insert into %s (%s) values ("%(self.name,",".join(order))
			sql += ",".join([self.formatVal(k, cols[k][j]) for k in order])
			sql += ");"
			ex(sql)

sets = []
#sets.append(DataSet("clothesdryer","cd",{"brand":"Brand","model":"Model No","star":"New Star","power":"New CEC"}))
#sets.append(DataSet("dishwashers","dw",{"brand":"Brand","model":"Model No","star":"New Star","power":"CEC_"}))
#sets.append(DataSet("clotheswashers","cw",{"brand":"Brand","model":"Model No","star":"New Star","power":"CEC_"}))
#sets.append(DataSet("fridgefreezer","ff",{"brand":"Brand","model":"Model No","star":"Star2009","power":"CEC_"}))
#sets.append(DataSet("televisions","tv",{"brand":"Brand_Reg","model":"Model_No","star":"Star","power":"CEC"}))
#sets.append(DataSet("computermonitors","cm",{"brand":"Brand Name","model":"Model Number","star":"Star Rating","power":"Comparative Energy Consumption"}))
sets.append(DataSet('airconditioner', 'ac', {'brand':'Brand','model':'Model_No','star':'Star2010_Heat','power':'H-Power_Inp_Rated'}))	

for sett in sets:
	ex(sett.dropString())
	ex(sett.createString())
	sett.insertString()

#fout.close()
#with open('c:\\wamp\\www\\data\\dump.txt', 'w') as fout:
#	fout.write(dset.createString())
