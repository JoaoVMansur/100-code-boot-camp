import requests
from dotenv import load_dotenv
import os
from datetime import datetime



load_dotenv()
today = datetime.today( )


#created pixela account 
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":os.getenv("PIXELA_TOKEN"),
    "username": os.getenv("PIXELA_USERNAME"),
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}
# response = requests.post(url=pixela_endpoint, json=user_params)


#create a new graph at pixela
headers = {
    "X-USER-TOKEN":os.getenv("PIXELA_TOKEN")
}
graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs"
graph_config = { 
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color":"kuro"
}
# response = requests.post(graph_endpoint, json=graph_config, headers=headers) 


#create a pixel 
pixel_creation_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPHID')}"
pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many pages did you read today?"),
}
# response = requests.post(pixel_creation_endpoint, json=pixel_params, headers=headers)

#update graph
update_graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPHID')}"
upated_params = {
    "name":"Reading Pages Counter this year"

}
# response = requests.put(url=update_graph_endpoint, json=upated_params, headers=headers)



#delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPHID')}/20230104"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)