import json
import requests
from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv()
username = value = os.environ.get('USERNAME')
password = value = os.environ.get('PASSWORDS')
image_ids_to_delete = []
auth = (username, password)
api_url = value = os.environ.get('APIURL')


def get_all_images(api_url, headers, limit=10000):
    try:
        params = {'limit': limit}
        response = requests.get(api_url, headers=headers, params=params, auth=auth)

        if response.status_code == 200:
            data = response.json()
            logger.info(f"Successfully retrieved data: {data}")
        else:
            logger.error(f"Failed to retrieve data. Status code: {response.status_code}")
        return data['result']

    except Exception as e:
        logger.error(f"Error making GET request: {e}")


def delete_images_by_ids(api_url, headers, image_ids):
    try:
        delete_url = f'{api_url}'
        payload = {"ids": image_ids}

        response = requests.delete(delete_url, headers=headers, json=payload, auth=auth)

        if response.status_code == 200:
            logger.info(f"Successfully deleted images with IDs: {image_ids}")
        else:
            logger.error(f"Failed to delete images. Status code: {response.status_code}")
            logger.error(response.text)

    except Exception as e:
        logger.error(f"Error making DELETE request: {e}")


if __name__ == "__main__":
    headers = {
        'Content-Type': 'application/json',
    }
    all_items = get_all_images(api_url, headers, limit=10000)
    for item in all_items:
        image_ids_to_delete.append(int(item['id']))
    delete_images_by_ids(api_url, headers, image_ids_to_delete)
