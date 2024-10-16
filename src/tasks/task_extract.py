import csv
from prefect import task
from config import config
import requests

from tasks.utils import handle_invalid_categoric

@task(name="Extraer información del csv")
def task_extract_csv(filename):
  data = []
  with open(filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      tmp_data = (row["categoria"], row["origen"], row["cantidad"])
      data.append(tmp_data)
  return data

@task(name="Extraer data de api foodishes")
def task_extract_food(categoria):
  print(categoria)
  response = requests.get("https://foodish-api.com/api/images/"+categoria)

  if response.status_code == 200:
      imagenes = response.json()["image"]
      print(imagenes)      
      return (imagenes)
      
  else:
    handle_invalid_categoric(categoria)
    pass