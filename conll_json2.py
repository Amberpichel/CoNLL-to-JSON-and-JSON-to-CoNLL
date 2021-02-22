import json
import glob
import os 
import sys

#usage command line: python json_conll.py input_folder

def get_paths(input_folder):
    """
    Stores all .txt files in a list
    Returns a list of strings of filepaths from the Text (volumes) folder
    :param inputfolder: inputfolder used in main
    """
    list_files = []
    conll_folder = glob.glob(input_folder + '/*.conll')
    
    for filename in conll_folder:
        list_files.append(filename)

    return list_files

def load_text(txt_path):
    """
    Opens the container en reads the elements(strings)
    Returns a string
    :param txt path: list with filepaths
    """
    with open(txt_path, 'rt') as infile:
        content = infile.readlines()
        
    return content

def process_all_txt_files(paths):
    """
    given a list of txt_paths
    -process each
    :param paths: list of content volume
    :return: list of dicts
    """
    list_dicts = []
    #strip newline, split on space char and make components for the dictionary
    for line in paths:
        components = line.rstrip('\n').split()
        if len(components) > 0:
            word = components[0]
            ner = components[1]
            predicted = ""
            feature_dict = {'word':word,
                            'ner': ner,
                            'predicted': predicted}
            components.append(feature_dict['predicted'])
            list_dicts.append(feature_dict)

    return list_dicts

def write_file(list_dicts, input_folder, text):
    """
    write volumes to new directory
    :param list_dicts: list_of dicts
    :param input_folder: folder with CONLL files
    :param text: pathname of CONLL file
    """
    directory = "json-dir"
    
    #check if directoy exists, if not make it
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    #get basename of the path and change extension to json
    base = os.path.basename(text)[:-6]
    json_str = '.json'
    basename = base + json_str
    
    #put in the new directory
    path = os.path.join (input_folder, directory)
    completeName = os.path.join(path, basename)
    
    #write file to json format
    jsondumps = json.dumps(list_dicts)
    jsonfile = open(completeName, "w")
    jsonfile.write(jsondumps)
    jsonfile.close()
            
def main():
    
    input_folder = sys.argv[1]
    
    #loop over every pathname and call functions for each path separately
    txt_path = get_paths(input_folder)
    for text in txt_path:
        paths = load_text(text)
        list_dicts = process_all_txt_files(paths)
        write_file(list_dicts, input_folder, text)

if __name__ == "__main__":
    main()
