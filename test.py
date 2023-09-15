import requests

BASE = "http://127.0.0.1:5000/"
headers = {'Content-Type': 'application/json'}

# data = [
#     {"likes": 84, "name" : "Rest API", "views" : 1000},
#     {"likes": 25, "name" : "Valorant", "views" : 15456},
#     {"likes": 10, "name" : "CS:GO", "views" : 8545}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), json=data[i], headers=headers)
#     print(response.json())
 
# input()
# response = requests.get(BASE + "video/5")
# data = response.json()
# print(data)

response = requests.patch(BASE + "video/2", json = {"views" : 99, "likes" : 965167935}, headers=headers)
if response.status_code == 200:
    print("Video views updated successfully.")
    print(response.json())
else:
    print("Error:", response.status_code)
    print("Response:", response.text)
