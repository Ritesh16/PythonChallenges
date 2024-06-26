import datetime

from service import Service
from dotenv import  load_dotenv
import os

# Load configuration
load_dotenv()
token=os.getenv("token")
user_name=os.getenv("user_name")

service = Service()
#service.create_user(token, user_name, "yes", "yes")

#service.create_graph(token, user_name, "3", "cycling", "Km", "float")

# Get graph as html
#service.get_graph(user_name, "graph1")

# add activity to graph
#service.add_value_graph(user_name, "graph1", "2.512", token)

date = datetime.datetime(2024, 4, 30).strftime("%Y%m%d")

#Update activity
#service.update_graph_value(user_name, "graph1", "20240430", token, "9.5")

#delete actibity
service.delete_pixel(user_name, "graph1", date, token)