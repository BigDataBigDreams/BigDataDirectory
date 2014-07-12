import csv
import json

with open("c:\\wamp\\www\\data\\2012.csv", "r") as csvFile, open("c:\\wamp\\www\\data\\2012.js", "w") as jsFile:
	reader = csv.reader(csvFile)
	prefix = "["
	for row in reader:
		colsToKeep = [row[0], row[1]]
		for j in [2, 17, 28, 29, 39, 65]:
			try:
				colsToKeep.append(int(row[j].replace(',', '')))
			except:
				colsToKeep.append(0)
		jsFile.write(prefix + json.dumps(colsToKeep))
		prefix = ",\n"
	jsFile.write("]")