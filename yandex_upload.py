import requests
from settings import TOKEN
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        file_path = os.path.normpath(file_path)
        params = {'path': file_path}

        response = requests.get(url, headers=headers, params=params)
        response_url = response.json()['href']
        response_upload = requests.put(response_url, headers=headers, data=open(file_path, 'rb'))
        if response_upload.status_code == 201:
            print('Загрузка прошла успешно')


if __name__ == '__main__':
    path_to_file = "for_upload/test_file.txt"
    uploader = YaUploader(TOKEN)
    uploader.upload(path_to_file)