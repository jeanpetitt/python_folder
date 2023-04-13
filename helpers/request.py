
import requests
import csv,os
import pandas as pd

path = f"{os.getcwd()}/dataset" 

# get urls of wikidata
def openUrL(query):

	url = "https://www.wikidata.org/w/api.php"

	query = query

	params = {
		"action": "wbsearchentities",
		"language": "en",
		"format": "json",
		"search": query

	}
	uri = ""
	try:

		data = requests.get(url, params=params)
		uri = data.json()["search"][0]["concepturi"]
	except:
		print("aucun resultat")

	return uri



def  openFilecsv(files):

	dataset = os.listdir(path)
	dataset.sort(reverse=False)
	header = ["File", "Col", "Row", "URI"]
	with open(files, "w+") as csv_file:
		writer = csv.writer(csv_file, delimiter=",")
		writer.writerow(header)
		# get filename from each file in dataset
		for file in dataset:

			if file.endswith(".csv"):
				total_rows = 0

				_file = pd.read_csv(f"{path}/{file}")
				total_cols=len(_file.axes[1])
				filename = file.split("_clean.csv")[0]

				with open(f"{path}/{file}", "r") as current_file:
					csv_reader = csv.reader(current_file)

					j = 0
					
					# compter le nombre de le fichier csv
					for rows in csv_reader:
						while j < len(rows):
							exec("col"+str(j)+"='"+rows[j]+"'") in locals(), globals()
							print(col0)
							j +=1
						total_rows +=1

					print("fichier:", filename, "nbre de ligne: ", total_rows, " nombre de col: ", total_cols)
					filetotalrowcol = total_rows * total_cols

					row = 0
					col = 0
					while row < filetotalrowcol:

						if row < total_rows:
							# uri = openUrL(current_file.loc[0][0])
							writer.writerow([filename, col, row])
							row += 1
						else:
							row = 0
							filetotalrowcol -= total_rows
							col += 1
					current_file.close()
			else:
				print("it is not csv file")
				
		csv_file.close()


	with open(files, "r") as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			print(row)
		csv_file.close()




openFilecsv("../test.csv")
