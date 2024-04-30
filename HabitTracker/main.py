from service import Service
from dotenv import  load_dotenv
import os

# Load configuration
load_dotenv()
token=os.getenv("token")
user_name=os.getenv("user_name")

service = Service()
#service.create_user(token, user_name, "yes", "yes")

service.create_graph(token, user_name, "3", "cycling", "Km", "float")