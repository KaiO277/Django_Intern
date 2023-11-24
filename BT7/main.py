import requests
import json

url = "https://qt.levanlau.net/api/course/course_category_level_1_get_all_not_auth_api"
response = requests.get(url)

if response.status_code == 200:

    data_list = response.json()

    print(data_list)
    print(type(data_list))
    
else:
    print("Yêu cầu API không thành công.")

print("===================================")
for item in data_list:
    print(item['id'])