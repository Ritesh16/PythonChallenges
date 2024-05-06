import requests
from datetime import datetime

class Service:
    pixela_endpoint = "https://pixe.la/v1/users"
    def __init__(self):
        pass

    def create_user(self, token: str, user_name: str, agree: str, notMinor: str):
        user_params = {
            "token": token,
            "username": user_name,
            "agreeTermsOfService": agree,
            "notMinor": notMinor
        }

        response = requests.post(url=self.pixela_endpoint, json=user_params)
        print(response.text)

    def create_graph(self, token: str, user_name: str, graph_id:str, graph_name: str, unit: str, type: str):
        graph_params = {
            "id": f"graph{graph_id}",
            "name": graph_name,
            "unit": unit,
            "type": type,
            "color": "shibafu"
        }

        headers = {
            "X-USER-TOKEN": token
        }

        graph_url = f"{self.pixela_endpoint}/{user_name}/graphs"

        response = requests.post(url=graph_url, json=graph_params, headers=headers)
        response.raise_for_status()
        print(response.text)

    def get_graph(self, user_name: str, graph_id: str):
        url = f"{self.pixela_endpoint}/{user_name}/graphs/{graph_id}"
        response = requests.get(url)
        print(response.text)

    def add_value_graph(self, user_name: str, graph_id : str, val: str, token:str):
        url = f"{self.pixela_endpoint}/{user_name}/graphs/{graph_id}"
        date = datetime.now().strftime("%Y%m%d")

        add_value_params = {
            "date" : date,
            "quantity": val
        }

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.post(url, json=add_value_params, headers=headers)

        response.raise_for_status()

    def update_graph_value(self, user_name: str, graph_id: str, date_to_update: str, token: str, new_value: str):
        update_endpoint = f"{self.pixela_endpoint}/{user_name}/graphs/{graph_id}/{date_to_update}"

        new_data = {
            "quantity": f"{new_value}"
        }

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.put(url=update_endpoint, json=new_data, headers=headers)
        response.raise_for_status()

    def delete_pixel(self, user_name: str, graph_id: str, date_to_update: str, token: str):
        delete_endpoint = f"{self.pixela_endpoint}/{user_name}/graphs/{graph_id}/{date_to_update}"

        headers = {
            "X-USER-TOKEN": token
        }

        response = requests.delete(url=delete_endpoint, headers=headers)

        print(response.text)



