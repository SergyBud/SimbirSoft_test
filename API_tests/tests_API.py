import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources/files'
TOKEN = 'AQAAAABjTYD6AADLW122Odnp10hsgDCEungMpnc'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


res = requests.get(f'{URL}?', headers=headers)
status = res.status_code
assert status == 200
print(status)
print(res.json())




# def get_info_about_folder():
#     """Получение всех папок и файлов"""
#     res = requests.get(f'{URL}?', headers=headers)
#     text_folder = res.text
#     status = res.status_code
#     return status, text_folder
#
# print(get_info_about_folder())



# def create_folder(path):
#     """Создание папки. \n path: Путь к создаваемой папке."""
#     requests.put(f'{URL}?path={path}', headers=headers)
#
# create_folder('hello world')
# create_folder('hello world/api')



    # result = ""
    # try:
    #     result = res.json()
    # except:
    #     result = res.text
    # return status, result






# def get_list_of_file(path):