import os, shutil

o_path = "/home/jeanpetit/Desktop/python/42"
o_csv = "/home/jeanpetit/Desktop/python/csv"

file_name = "file"
i=1
a_paths = f"{os.getcwd()}/annotated" 

if "__main__":
	
	folder_path = os.listdir(o_path)

	for file in folder_path:
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
		csv_path = os.listdir(o_csv)
		for csv_file in csv_path:
			shutil.copy(f"{o_csv}/{csv_file}", current_folder_wikidata)
			shutil.copy(f"{o_csv}/{csv_file}", current_folder_foodon)

		# get file to annotate and rename it to file_clean and put it in outputfolder
		shutil.copy(f"{o_path}/{file}", current_folder_output)

		# copy file csv to annotate in the input folder
		shutil.copy(f"{o_path}/{file}", current_folder_input)
		
		i += 1

	


			