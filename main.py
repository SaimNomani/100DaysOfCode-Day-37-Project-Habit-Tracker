import requests
from datetime import datetime
from data import TOKEN, USERNAME
graph_id='graph1'
pixela_endpoint="https://pixe.la/v1/users"
# setting up user
user_parameters={
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# user_response=requests.post(url=pixela_endpoint, json=user_parameters)
# print(user_response.text)

# setting up graph
graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'
graph_configuration={
    'id': graph_id,
    'name': "Coding graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}
# advance authentication
headers={
    "X-USER-TOKEN": TOKEN,
}
# graph_response=requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(graph_response.text)

# posting pixel to graph
post_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
today=datetime(year=2023, month=11, day=13)
pixel_configuration={
    "date": today.strftime('%Y%m%d'),
    "quantity": '120',
}
# pixel_response=requests.post(url=post_pixel_endpoint, json=pixel_configuration, headers=headers)
# print(pixel_response.text)

# update pixels
update_pixel_endpoint=f"{post_pixel_endpoint}/20231113"
update_params={
    "quantity": "60"
}
# update_pixel_response=requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(update_pixel_response.text)

# delete pixel
delete_pixel_endpoint=f"{post_pixel_endpoint}/20231113"
delete_pixel_response=requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel_response.text)