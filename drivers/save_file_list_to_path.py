import os

def save_folders_to_file(directory, file_path):
    folders = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            folders.append(os.path.join(dirpath, dirname))

    
    folders = list(map(lambda x: x.replace("data/single_snapshots/", ""), folders))

    with open(file_path, "w") as file:
        for folder in folders:
            file.write(folder + "\n")

save_folders_to_file("data/single_snapshots/","data/url_ids.txt")
