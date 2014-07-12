import csv

class DataSet:
	def __init__(self, name, pref, keys):
		self.name = name
		self.keys = keys
		self.pref = pref
		
	def createString(self):
		s = "create table %(name)s ("
		s += "%(pref)s_id int not null auto increment,"
		s += "%(pref)s_brand varchar(32),"
		s += "%(pref)s_model varchar(32),"
		s += "%(pref)s_power decimal(4,2),"
		s += "%(pref)s_star tinyint,"
		s += "PRIMARY KEY (%(pref)s_id));"
		return s %({'name':self.name,'pref':self.pref})
		
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

keys = {'brand':'Brand','model':'Model_No','star':'Star2010_Heat','power':'H-Power_Inp_Rated'}
dset = DataSet('airconditioner', 'ac', keys)
print(dset.colArray())
