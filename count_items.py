import json
import requests
from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv()
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORDS')
image_ids_to_delete = []
auth = (username, password)
api_url = os.environ.get('APIURL')


def get_all_images(api_url, headers, limit=10000):
    try:
        params = {'limit': limit}
        response = requests.get(api_url, headers=headers, auth=auth, params=params)

        if response.status_code == 200:
            data = response.json()
            logger.info(f"Successfully retrieved data: {data}")
        else:
            logger.error(
                f"Failed to retrieve data. Status code: {response.status_code}")
            return []

        return data['result']

    except Exception as e:
        logger.error(f"Error making GET request: {e}")
        return []

# Example usage:
headers = {'Content-Type': 'application/json'}  # Adjust headers as needed
result = get_all_images(api_url, headers, limit=10000)


items = []
for item in result:
    items.append(item["metadata"]["identification"])

print(len(items))

items_tupe = set(items)    
print(len(items_tupe))
