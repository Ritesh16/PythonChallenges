import requests

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
        print(graph_url)

        response = requests.post(url=graph_url, json=graph_params, headers=headers)
        response.raise_for_status()
        print(response.text)