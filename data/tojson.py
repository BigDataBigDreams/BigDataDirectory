import csv
import json

with open("c:\\wamp\\www\\data\\2012.csv", "r") as csvFile, open("c:\\wamp\\www\\data\\2012.js", "w") as jsFile:
	reader = csv.reader(csvFile)
	jsFile.write('[["Fine Industry","Broad Industry","Number","Income"]')
	for row in reader:
		colsToKeep = [row[0], row[1]]
		for j in [2,4]:
			try:
				colsToKeep.append(int(row[j].replace(',', '')))
			except:
				colsToKeep.append(0)
		jsFile.write(',')
		jsFile.write(json.dumps(colsToKeep))
		
	jsFile.write("]")