import requests

url = "https://qt.levanlau.net/api/course/course_category_level_1_get_all_not_auth_api"

response = requests.get(url)


print(response.text)
