
import os
from opensea import OpenseaAPI
import pandas as pd
import time
def get_slug_data(project_name):


# Replace YOUR_API_KEY with your OpenSea API key
	api_key = # opensea_api_key


	# Replace PROJECT_NAME with the name of the NFT project you want to query


	# Initialize the OpenSea client
	client = OpenseaAPI(apikey=api_key)


	# Query the OpenSea API to get the contract address and website of the NFT project
	response = client.collection(collection_slug=project_name)
	#print(response)
	



	# # Check if the API request was successful
	# if response.status_code == 200:
	#     # Get the contract address and website from the API response
	#     data = response.json()
	#     contract_address = data["results"][0]["asset_contract"]["address"]
	#     website = data["results"][0]["external_link"]

	#     print(f"Contract address: {contract_address}")
	#     print(f"Website: {website}")
	# else:
	#     print("API request failed")



	website=response['collection']['primary_asset_contracts'][0]['address']
	contract_address=response['collection']['primary_asset_contracts'][0]['external_link']
	open_sea_link=f"https://opensea.io/collection/{project_name}"
	twitter_username=response['collection']['twitter_username']
	if(str(twitter_username)=="None"):
		twitter_link=None
	else:
		twitter_link=f"https://twitter.com/{twitter_username}"

	file=open("1k_slug_data.csv","a")
	file.write(f"{project_name},{contract_address},{open_sea_link},{website},{twitter_link}\n")
	file.close()


count=0
df=pd.read_csv("slugs.csv")
for index,row in df.iterrows():
	count=count+1
	time.sleep(1)
	project_name=row['slug_name']
	print(f"Progress:{count}/1000, checking {project_name}")
	try:
		get_slug_data(project_name)
	except Exception as e:
		print(e)



