import json
import glob
import os 
import sys
import csv

#NOTES: 
#usage command line: python json_conll.py input_folder

def get_paths(input_folder):
    """
    Stores all .txt files in a list
    Returns a list of strings of filepaths from the Text (volumes) folder
    :param inputfolder: inputfolder used in main
    """
    list_files = []
    conll_folder = glob.glob(input_folder + '/*.json')
    
    for filename in conll_folder:
        list_files.append(filename)

    return list_files

def load_text(txt_path):
    """
    Opens the container en reads the elements(strings)
    Returns a string
    :param txt_path: list with filepaths
    """
    with open(txt_path, 'r') as json_file:
        data = json_file.read()
        content = json.loads(data)
    
    return content

def process_and_write(loaded_dicts, input_folder, text):
    """
    Process each CONLL and write to file
    :param paths: content of json file
    :param input_folder: folder with json files
    :param text: pathname of json file
    """
    directory = 'conll-dir'
    
    #check if dir exists, if not make one
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    #get basename of path and change extension to '.conll'
    base = os.path.basename(text)[:-5]
    conll_str = '.conll'
    basename = base + conll_str
    
    #add directory with files to the input folder
    path = os.path.join(input_folder, directory)
    complete_name = os.path.join(path, basename)
    
    #open write file
    f = csv.writer(open(complete_name, 'w'), delimiter=(' '))
    
    #for every value in the json dict, add values to list and write list
    for json_dict in loaded_dicts:
        values_list = []
        for key, value in json_dict.items():
            values_list.append(value)
                
        f.writerow(values_list)
        
def main():
    
    input_folder = sys.argv[1] 
    
    txt_path = get_paths(input_folder)
    for text in txt_path:
        loaded_dicts = load_text(text)
        process_and_write(loaded_dicts, input_folder, text)

if __name__ == "__main__":
    main()
