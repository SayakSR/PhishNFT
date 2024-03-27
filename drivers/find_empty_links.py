import os
from bs4 import BeautifulSoup
import time
import re

def empty_links(project_name):
    folder_path = f'data/single_snapshots/{project_name}' # replace with the actual path to the folder
    empty_links = []
    print(f"Checking {project_name}")
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                html = f.read()
                soup = BeautifulSoup(html, 'html.parser')
                for link in soup.find_all('a', href=True):
                    if not link['href']:
                        empty_links.append({"title": link.get_text(), "href": link['href']})

    print(empty_links)
    #time.sleep(2)




def twitter_opensea_links(project_name):

    # specify the directory to search
    directory = f'data/single_snapshots/{project_name}' 
    # regular expressions for Twitter and OpenSea links
    twitter_pattern = re.compile(r'https?://(www\.)?twitter\.com/[a-zA-Z0-9]+')
    opensea_pattern = re.compile(r'https?://(www\.)?opensea\.io/[a-zA-Z0-9]+')

    # search for HTML files in the directory
    for filename in os.listdir(directory):
        print(f"Checking {project_name}")
        if filename.endswith('.html'):

            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                # search for Twitter and OpenSea links in the file
                for match in re.finditer(twitter_pattern, content):
                    print(f'Twitter link found in {filename}: {match.group(0)}')
                for match in re.finditer(opensea_pattern, content):
                    print(f'OpenSea link found in {filename}: {match.group(0)}')


with open("data/url_ids.txt", "r") as file:
    url_list = [line.rstrip("\n") for line in file.readlines()]


for i in url_list:
    try:
        # empty_links(i)
        twitter_opensea_links(i)
    except Exception as e:
        print(e)
