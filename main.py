import os, shutil

o_path = f"{os.getcwd()}/source" 
o_csv = f"{os.getcwd()}/csv" 
a_path = f"{os.getcwd()}/INF4188" 
r_path = f"{os.getcwd()}/releven_src" 
ir_path = f"{os.getcwd()}/irreleven_src" 
a_paths = f"{os.getcwd()}/annotated" 
clean_f = f"{os.getcwd()}/clean" 
src_clean_f = f"{os.getcwd()}/source_clean"



# generer la struction du dossier INF4188
def generate_structure(folder_paths):
	i = 0
	file_name = "file"
	csv_path = os.listdir(o_csv)
	for file in folder_paths:
		for csv_file in csv_path:
			shutil.copy(f"{o_csv}/{csv_file}", f"{a_paths}/{file}/output/wikidata")
			shutil.copy(f"{o_csv}/{csv_file}", f"{a_paths}/{file}/output/foodon")

		downloaded_file_path = f"{a_paths}/{file_name}{i}"
		os.makedirs(downloaded_file_path)

		# input and output folder
		# get current folder that we have created
		current_folder_input = f"{downloaded_file_path}/input"
		current_folder_output = f"{downloaded_file_path}/ouput"
		os.makedirs(current_folder_output)
		os.makedirs(current_folder_input)

		# in output folder create the output wikidata and foodon folder
		current_folder_wikidata = f"{current_folder_output}/wikidata"
		current_folder_foodon = f"{current_folder_output}/foodon"
		os.makedirs(current_folder_wikidata)
		os.makedirs(current_folder_foodon)

		# copy cta.csv, cea.csv and cpa.csv empty in each folder input
		for csv_file in csv_path:
			shutil.copy(f"{o_csv}/{csv_file}", current_folder_wikidata)
			shutil.copy(f"{o_csv}/{csv_file}", current_folder_foodon)

		# get file to annotate and rename it to file_clean and put it in outputfolder
		shutil.copy(f"{o_path}/{file}", current_folder_output)

		# copy file csv to annotate in the input folder
		shutil.copy(f"{o_path}/{file}", current_folder_input)
		i += 1

# function to get relevant file and irreleven
def get_relevent(folder_path):
	folder_cleaned = []
	folder_not_cleaned = []

	for folder in folder_path:
		# obtenir le chemin des dossier input et output se trouvant a l'interieur de chaque dossier dans INF4188
		output_f = f"{os.getcwd()}/INF4188/{folder}/output"
		input_f = f"{os.getcwd()}/INF4188/{folder}/input"

		# lister les fichier et dossier dans input et outpus
		folder_lis_o = os.listdir(output_f)
		folder_lis_i = os.listdir(input_f)
		r_folder = os.listdir(r_path)
		ir_folder = os.listdir(ir_path)


		# parcourir chaque fichier input 
		for subF in folder_lis_i:
			# pour chaque element dans le input
			for file in folder_lis_o:
				# si l'element est un fichier
				if os.path.isfile(f"{output_f}/{file}"):
					# si ce fichier n'est pas dans la liste des relevent
					if subF not in r_folder:
						# copier ce fichier dans la liste releven
						shutil.copy(f"{input_f}/{subF}", r_path)
					# ajouter le dossier courant a la liste des dossier ayant des fichier cleanable
					folder_cleaned.append(folder)
		
		# si le dossier courant n'est pas dans la liste clean 
		if folder not in folder_cleaned:
			# ajouter ce dossier dans la liste des dossier possedant des fichiers non cleanable
			folder_not_cleaned.append(folder)

	folder_not_cleaned.sort(reverse=False)
						
	print(folder_not_cleaned)
					

# get irrevelen file
def get_irrelevent(folder_source):

	releven_folder = os.listdir(r_path)

	for file in folder_source:
		if file not in releven_folder:
			shutil.copy(f"{o_path}/{file}", ir_path)




# get cleaned file

def get_cleaned_file(folder_path):
	src_clean_path = os.listdir(clean_f)

	for folder in folder_path:
		# obtenir le chemin des dossier input et output se trouvant a l'interieur de chaque dossier dans INF4188
		output_f = f"{os.getcwd()}/INF4188/{folder}/output"

		folder_lis_o = os.listdir(output_f)

		# parcourir chaque fichier input 
		for subF in folder_lis_o:
			# si le subF est un fichier on le copie dans clean
			if os.path.isfile(f"{output_f}/{subF}"):
				if subF not in src_clean_path:
					shutil.copy(f"{output_f}/{subF}", clean_f)
						

#  copier les fichier source des input du dossier INF4188 dans le dossier src_clean
def copy_file(folder_path):
	double_file = []
	i = 0
	src_clean_path = os.listdir(src_clean_f)
	for folder in folder_path:
		# obtenir le chemin des dossier input et output se 
		# trouvant a l'interieur de chaque dossier dans INF4188
		input_f = f"{os.getcwd()}/INF4188/{folder}/input"

		# lister les fichier et dossier dans input et outpus
		folder_lis_i = os.listdir(input_f)

		# parcourir chaque fichier input 
		for subF in folder_lis_i:
			if len(folder_lis_i) >=2:
				print("dossier", folder, "input")
			# si le subF est un fichier on le copie dans source_clean
			if os.path.isfile(f"{input_f}/{subF}"):
				if subF in src_clean_path:
					double_file.append(subF)
				else:
					shutil.copy(f"{input_f}/{subF}", src_clean_f)
					i=i+1
		# print(i, double_file)


# copier les fichiers dans source_clean qui sont dans src mais ne sont pas dans source_clean
def copy_file_absent(folder_paths):
	src_clean_path = os.listdir(src_clean_f)
	for folder in folder_paths:
		if folder not in src_clean_path:
			# shutil.copy(f"{o_path}/{folder}", src_clean_f)
			print("absent file",folder)


if "__main__":
	
	folder_source = os.listdir(src_clean_f)
	folder_path = os.listdir(a_path)
	

	copy_file(folder_path)
	# copy_file_absent(folder_source)
	get_relevent(folder_path)
	get_cleaned_file(folder_path)
	get_irrelevent(folder_source)





	


			