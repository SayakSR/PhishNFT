import os 
driver_files = [f[:-3] for f in os.listdir('drivers') if f.endswith('.py') and f != '__init__.py']

import importlib

for module_name in driver_files:
    full_module_name = f'drivers.{module_name}'
    
    imported_module = importlib.import_module(full_module_name)

import csv

# Feature 1: matches_official_slug_url

def check_match(url,csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_url = row['url']
            if url == csv_url:
                print("URL matched!")
                return
    print("URL not found.")

# Example usage
#check_match("http://alphagirlclub.io","1k_slug_data.csv")


# Get contract address, and Feature 3:No_of_ether_addresses


contract_address, no_of_eth_addresses = eth_address_tracker(ether_address)
print(contract_address)
print(no_of_eth_addresses)

#time.sleep(10)


#Feature 2: If_official_contract_address


def check_contract(contract_address, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_contract = row['contract']
            if contract_address.lower() == csv_contract.lower():
                print("Contract address matched!")
                return
    print("Contract address not found.")

# Example usage
#check_contract("0x47a00fc8590c11be4c419d9ae50dec267b6e24ee", "1k_slug_data.csv")


# Feature 3: No_of_ether_addresses

import os
import re

def count_eth_addresses(directory):
    
    eth_regex = re.compile(r"0x[a-fA-F0-9]{40}")
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r") as file:
                try:
                    #print(f"Checking file {filepath}")
                    content = file.read()
                    matches = eth_regex.findall(content)
                    for match in matches:
                        if match.count("0") >= 10 or match.count("f") >= 10:
                            pass
                        else:
                            file=open(f"temp.txt","a")
                            file.write(f"{match}\n")
                            file.close()
                except Exception as e:
                    pass
    with open("temp.txt", 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        print(num_lines)
    os.remove("temp.txt")

# Example usage
#count_eth_addresses("data/1658559773/")

# =================================================

#Feature 7: If_twitter_unavailable
# Feature 10: No_of_twitter_followers
# Feature 11: Twitter_age

def twitter_suspended_removed_follower_age(url):
    import re
    from datetime import datetime


    user_active=0

    import tweepy

    username = re.findall(r"(?<=twitter.com/)\w+", url)[0]
    consumer_key = # Twitter V2 consumer key
    consumer_secret = # Twitter V2 consumer secret
    access_token = # Twitter V2 access_token
    access_token_secret =  # Twitter V2 access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        user = api.get_user(username)
        print(f"{username} is not suspended or removed.")
        user_active=1
    except tweepy.error.TweepError as e:
        if e.api_code == 63:
            print(f"{username} is suspended.")
            user_active=0
        elif e.api_code == 34:
            print(f"{username} does not exist.")
            user_active=0

        else:
            print(f"Error: {e}")
            user_active=0

    # Check no of followers
    if(user_active==1):
        try:
            print(f"{username} has {user.followers_count} followers.")
            followers=user.followers_count

        except tweepy.error.TweepError as e:
            print(f"Error: {e}")
            followers=0

        try:
            account_age = datetime.now() - datetime.strptime(user.created_at.strftime("%Y-%m-%d"), "%Y-%m-%d")
            print(f"{username} account age is {account_age.days} days.")
            age=account_age.days
        except tweepy.error.TweepError as e:
            print(f"Error: {e}")
            age=0
    else:
        followers=0
        age=0

# ===============================================


import os
import re

# Feature 5: If Twitter_link, Feature 6: Opensea_link, 
# Feature 8: Twitter_page_is_same, Feature 9: Opensea_page_is_same
# Feature 7: If_twitter_unavailable

def twitter_opensea_links(directory,csv_file):

    twitter_links=[]
    opensea_links=[]

    # specify the directory to search
    
    # regular expressions for Twitter and OpenSea links
    twitter_pattern = re.compile(r'https?://(www\.)?twitter\.com/[a-zA-Z0-9]+')
    opensea_pattern = re.compile(r'https?://(www\.)?opensea\.io/[a-zA-Z0-9]+')

    # search for HTML files in the directory
    for filename in os.listdir(directory):
        
        if filename.endswith('.html'):

            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                # search for Twitter and OpenSea links in the file
                for match in re.finditer(twitter_pattern, content):
                    twitter_link=match.group(0)
                    twitter_links.append(twitter_link)
                for match in re.finditer(opensea_pattern, content):
                    opensea_link=match.group(0)
                    opensea_links.append(opensea_link)
    print(twitter_links)
    print(opensea_links)

    # Check if twitter links match 1k official twitter links

    with open(csv_file, 'r') as file:
        flag=0
        reader = csv.DictReader(file)
        for row in reader:
            csv_twitter = row['twitter']
            for link in twitter_links:
                if link == csv_twitter:
                    print(f"Link {link} matched with {csv_twitter} in the csv file.")
                    flag=1
                    
        if(flag==0):
            print("No match found.")

        # check if Twitter link is removed or suspended

        for link in twitter_links:
            twitter_suspended_removed(link)

    # Check if opensea links match 1k official opensea links


    with open(csv_file, 'r') as file:
        flag=0
        reader = csv.DictReader(file)
        for row in reader:
            csv_opensea = row['opensea']
            for link in opensea_links:
                if link == csv_opensea:
                    print(f"Link {link} matched with {csv_opensea} in the csv file.")
                    flag=1
                    
        if(flag==0):
            print("No match found.")



# Example usage
#twitter_opensea_links("data/1658559773/","1k_slug_data.csv")



