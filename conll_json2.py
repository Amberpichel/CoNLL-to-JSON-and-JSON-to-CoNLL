import json
import glob
import os 

def get_paths(input_folder):
    """
    Stores all .txt files in a list
    Returns a list of strings of filepaths from the Text (volumes) folder
    """
    list_files = []
    for filename in glob.glob('../text/*.conll'):
        list_files.append(filename)

    return list_files

def load_text(txt_path):
    """
    Opens the container en reads the elements(strings)
    Returns a string
    """
    with open(txt_path, 'rt') as infile:
        content = infile.readlines()
        
    return content

def process_all_txt_files(paths):
    """
    given a list of txt_paths
    -process each
    :param list txt_paths: list of paths to txt files 
    :return: list of dicts
    """
    list_dicts = []
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

def write_file(list_dicts, text, dir_exists = False):
    """
    write volumes to new directory
    :param list_dicts: list_of dicts
    """
    
    if dir_exists == True:
        replace_txt = text.replace("../text/", "")
        basename = replace_txt+".json"
    
        directory = "test-dir"
        parent_dir = '../text/'
        path = os.path.join(parent_dir, directory)
        completeName = os.path.join(path, basename)
    
        jsondumps = json.dumps(list_dicts)
        jsonfile = open(completeName, "w")
        jsonfile.write(jsondumps)
        jsonfile.close()
    
    if dir_exists == False:
        directory = "test-dir"
        if os.path.isdir(directory) == True:
            print('File exists: Set param overwrite_exisiting_conll_file to True if you want to overwrite it')
        elif os.path.isdir(directory) == False:
            os.mkdir(directory)
            
def main():
    """
    convert from conll to json for all the separate volumes
    """
    
    output_dir = '../test_dir'
    input_folder = '../text'

    txt_path = get_paths(input_folder)
    for text in txt_path:
        paths = load_text(text)
        list_dicts = process_all_txt_files(paths)
        write_file(list_dicts, text)

main()
