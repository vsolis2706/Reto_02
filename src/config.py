import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  MYSQL_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : os.getenv("BD_PASSWORD"),
    "database" : "db_fooddishes"
  }

  ENDPOINTS = {
    "food" : "https://foodish-api.com/api/images/"
  }



config = Config()