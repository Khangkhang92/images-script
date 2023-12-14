import os
import pandas as pd
import base64
import requests
from loguru import logger
import json
from dotenv import load_dotenv


load_dotenv()

username = value = os.environ.get('USERNAME')
password = value = os.environ.get('PASSWORDS')
api_url = value = os.environ.get('APIURL')
image_ids_to_delete = []
auth = (username, password)


def make_api_call(image_base64, metadata):
    headers = {
        'Content-Type': 'application/json',

    }
    metadata = {key: str(value) if isinstance(value, float)
                else value for key, value in metadata.items()}
    payload = {
        "image": {
            "base64": image_base64,
            "metadata": metadata
        }
    }

    response = requests.post(api_url, json=payload, headers=headers, auth=auth)
    if response.status_code == 200:
        logger.info(f"API call successful for image with metadata: {metadata}")
    else:
        logger.error(f"API call failed. Status code: {response.status_code}")
        logger.error(response.text)


excel_file_path = 'DS ĐK TRAO GIẢI SEAMO.xlsx'
df = pd.read_excel(excel_file_path)

for index, row in df.iterrows():
    folder_name = str(row['Số báo danh'])

    folder_path = os.path.join(os.getcwd(), f'Anh/{folder_name}')

    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif']):
                with open(file_path, 'rb') as image_file:
                    image_data = base64.b64encode(
                        image_file.read()).decode('utf-8')
                if row['Thành tích'] is None:
                    medal = 'Chào mừng bạn đến với kỳ thi SEAMO'
                else:
                    medal = row['Thành tích']
                metadata = {
                    "name": row['Họ tên thí sinh'],
                    "class": str(row['Lớp']),
                    "identification": row['Số báo danh'],
                    "dob": str(row['Ngày Tháng Năm sinh']),
                    "school": row['Trường'],
                    "subject": "Toán",
                    "medal": medal
                }

                make_api_call(image_data, metadata)
                image_data = metadata = None

    else:
        logger.warning(
            f"Folder '{folder_name}' not found in the specified directory.")
