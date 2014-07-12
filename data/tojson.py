import csv
import json

with open("mycsv.csv", "r") as csvFile, open("myjs.js", "w") as jsFile:
	reader = csv.reader(csvFile)
	prefix = "["
	for row in reader:
		rowsToKeep = [row[j] for j in [0, 1, 2, 17, 28, 29, 39, 65]]
		jsFile.write(prefix + json.dumps(rowsToKeep))
		prefix = ",\n"
	jsFile.write("]")
	