import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources?path=%2F'
TOKEN = 'AQAAAABjTYD6AADLW122Odnp10hsgDCEungMpnc'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

res = requests.get(URL, headers=headers)
status = res.status_code
assert status == 200
if res.status_code == 200:
    r = res.json()
    for i in r.get("_embedded").get("items"):
        print(i.get("name"))

print(status)
print(res.json())

"""Второй вариант был с использованием рекурсивной функции для отображения всех файлов  и папок и всех файлов 
и папок внутри прочих папок, но, к сожалению , не хватило времени закончить"""

#
# URL = 'https://cloud-api.yandex.net/v1/disk/resources?path='
# TOKEN = 'AQAAAABjTYD6AADLW122Odnp10hsgDCEungMpnc'
# headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

# def func(a, suburl="%2F"):
#
#     if a.get("type") != 'dir':
#         print(a.get("name"))
#     elif a.get("type") == 'dir':
#         urls = f'{a.get("name")}%2F'
#         print(a.get("name"))
#         res1 = requests.get(URL + suburl + urls, headers=headers)
#         status1 = res1.status_code
#         assert status1 == 200
#         for j in res1.json().get("_embedded").get("items"):
#             # if j.get("type") != "dir":
#             #     print(a.get("name") + "/" + j.get("name"))
#             # if j.get("type") == "dir":
#             print(a.get("name") + "/" + j.get("name"))
#         for u in res1.json().get("_embedded").get("items"):
#             if u.get("type") == "dir":
#                 print(u.get("name") + "/" + j.get("name"))
#                 urls = f'%2F{a.get("name")}%2F'
#                 func(j, urls)
#             else:
#                 continue
#
# h = {}
#
# def func(a):
#     b = a.json().get("_embedded").get("items")
#     for w in b:
#         if w.get("type") != 'dir':
#             h[w.get('name')] = 'file'
#         elif w.get("type") == 'dir':
#             h[w.get('name')] = {}
#             res1 = requests.get(f'{URL}%2F{w.get("name")}%2F', headers=headers)
#             print(f'{URL}%2F{w.get("name")}%2F')
#             status1 = res.status_code
#             assert status1 == 200
#             func(res1)
# res = requests.get(URL + "%2F", headers=headers)
# status = res.status_code
# assert status == 200
# _r = res.json()
# print(_r)
# d = _r.get("_embedded")
# # for i in d.get("items"):
# func(res)
# print(h)
# if i.get("type") == "dir":
#     print(i.get("name"))
#     res = requests.get(f'{URL}{i.get("name")}', headers=headers)
#     status = res.status_code
#     assert status == 200
#     for j in res.json().get("_embedded").get("items"):
#         print("   |_"+j.get("name"))
# else:
#     print(i.get("name"))





# URL = 'https://cloud-api.yandex.net/v1/disk/resources/files'
# TOKEN = 'AQAAAABjTYD6AADLW122Odnp10hsgDCEungMpnc'
# headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
#
#
# res = requests.get(f'{URL}?', headers=headers)
# status = res.status_code
# assert status == 200
# print(status)
# print(res.json())


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

