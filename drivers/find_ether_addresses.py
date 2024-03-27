import os
import re
import time

def is_contract_address(address):
    if not address.startswith('0x'):
        return False
    # Check if the address has a length of 42 characters
    if len(address) != 42:
        return False
    # Check if the address contains only hexadecimal characters
    if not all(c in '0123456789abcdefABCDEF' for c in address[2:]):
        return False
    # If all true, it is likely a contract address
    return True



def find_eth_addresses(directory,url_id):
    print(f"Checking URL id:{url_id}")
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
                        if match.count("0") >= 10 or match.count("f") >= 10 or match.count("0xfff") >= 1:
                            pass
                        else:
                            
                            if is_contract_address(match):
                                #print(f"{match} is a contract address.")
                                file=open(f"addresses/{url_id}.txt","a")
                                file.write(f"{match}\n")
                                file.close()
                            else:
                                print(f"{match} is a token address.")
                                
                            
                except Exception as e:
                    print(e)

def remove_duplicate_lines(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    with open(filepath, 'w') as f:
        seen = set()
        for line in lines:
            line=line.lower()
            if line not in seen:
                f.write(line)
                seen.add(line)



with open("url_ids.txt", "r") as file:
    url_list = [line.rstrip("\n") for line in file.readlines()]


for i in url_list:
    find_eth_addresses(f"data/single_snapshots/{i}",i)
    try:
        remove_duplicate_lines(f"data/addresses/{i}.txt")
    except:
        pass

