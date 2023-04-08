import os, shutil

o_path = f"{os.getcwd()}/source" 
o_csv = f"{os.getcwd()}/csv" 

a_path = f"{os.getcwd()}/INF4188" 
file_name = "file"
i=0
a_paths = f"{os.getcwd()}/annotated" 
clean_f = f"{os.getcwd()}/clean" 
src_clean_f = f"{os.getcwd()}/source_clean"

double_file = []

if "__main__":
	
	folder_paths = os.listdir(o_path)

	folder_path = os.listdir(a_path)

	csv_path = os.listdir(o_csv)
	src_clean_path = os.listdir(src_clean_f)

	
	#  copier les fichier source dans le input du dossier INF4188 dans le dossier src_clean
	for folder in folder_path:
		# obtenir le chemin des dossier input et output se trouvant a l'interieur de chaque dossier dans INF4188
		output_f = f"{os.getcwd()}/INF4188/{folder}/output"
		input_f = f"{os.getcwd()}/INF4188/{folder}/input"

		# lister les fichier et dossier dans input et outpus
		folder_lis_o = os.listdir(output_f)
		folder_lis_i = os.listdir(input_f)

		# parcourir chaque fichier input 
		for subF in folder_lis_i:
			if subF == "KNSR4221_5.csv":
				print(f"{os.getcwd()}/INF4188/{folder}/input/{subF}")
			# si le subF est un fichier on le copie dans source_clean
			if os.path.isfile(f"{input_f}/{subF}"):
				if subF in src_clean_path:
					double_file.append(subF)
				else:
					shutil.copy(f"{input_f}/{subF}", src_clean_f)
					i=i+1

					
	print(i, double_file)
	# copier les fichiers dans source_clean qui sont dans src mais ne sont pas dans source_clean
	for folder in folder_paths:
		if folder not in src_clean_path:
			# shutil.copy(f"{o_path}/{folder}", src_clean_f)
			print("absent file",folder)

	# classons les ficher releven et irreleven

	# for file in folder_path:
	# 	for csv_file in csv_path:
	# 		shutil.copy(f"{o_csv}/{csv_file}", f"{a_paths}/{file}/output/wikidata")
	# 		shutil.copy(f"{o_csv}/{csv_file}", f"{a_paths}/{file}/output/foodon")

	
		# downloaded_file_path = f"{a_paths}/{file_name}{i}"
		# os.makedirs(downloaded_file_path)

		# # input and output folder
		# # get current folder that we have created
		# current_folder_input = f"{downloaded_file_path}/input"
		# current_folder_output = f"{downloaded_file_path}/ouput"
		# os.makedirs(current_folder_output)
		# os.makedirs(current_folder_input)

		# # in output folder create the output wikidata and foodon folder
		# current_folder_wikidata = f"{current_folder_output}/wikidata"
		# current_folder_foodon = f"{current_folder_output}/foodon"
		# os.makedirs(current_folder_wikidata)
		# os.makedirs(current_folder_foodon)

		# # copy cta.csv, cea.csv and cpa.csv empty in each folder input
		# csv_path = os.listdir(o_csv)
		# for csv_file in csv_path:
		# 	shutil.copy(f"{o_csv}/{csv_file}", current_folder_wikidata)
		# 	shutil.copy(f"{o_csv}/{csv_file}", current_folder_foodon)

		# # get file to annotate and rename it to file_clean and put it in outputfolder
		# shutil.copy(f"{o_path}/{file}", current_folder_output)

		# # copy file csv to annotate in the input folder
		# shutil.copy(f"{o_path}/{file}", current_folder_input)
		# i += 1

	


			