from prefect import flow

from tasks.task_extract import task_extract_csv, task_extract_food
from tasks.task_load import task_load_food
from tasks.task_util import task_get_food_from_db, task_init_table
from tasks.utils import handle_invalid_categoric, validate_categoric

BASELINE_TASKS = True
DATA_PATH = "./resources/data.csv"

@flow(name="ETL FOOD DISHES", log_prints=True)
def main_flow():

  if BASELINE_TASKS:
    task_init_table()

  initial_food_data = task_extract_csv(DATA_PATH)

  for food in initial_food_data:
    categoria = food[0]   
    origen = food[1]  
    cantidad = food[2]

    print(categoria)
    if validate_categoric(categoria):
      print(categoria)
      food_exists = task_get_food_from_db(categoria)
      print(food_exists)
      if not food_exists:
        print("no exite la comida")
        print(food_exists)
        api_food_data = task_extract_food(categoria)
        print(api_food_data)
        food_data = (categoria, origen, api_food_data ,cantidad)
        task_load_food(food_data)
    else:
      handle_invalid_categoric(categoria)
      pass


if __name__ == "__main__":
  main_flow()
