from prefect import task
from config import config
from mysql import connector

@task(name="Inicializar la tabla de food")
def task_init_table():
  try: 
    with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
          query_drop_table = "drop table if exists food"

          cursor.execute(query_drop_table)
          db.commit()

          query_create_table = """
          create table if not exists food(
            id int auto_increment primary key,
            categoria varchar(255),           
            origen varchar(255),
            foto varchar(255),
            cantidad int
          )
          """
          cursor.execute(query_create_table)
          db.commit()
  except Exception as error:
     print("error: ", error)

@task(name="Consultar la existencia del plato de comida en la db")
def task_get_food_from_db(categoria):
   with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
         query_select_one = "select * from food where categoria = %s"
         cursor.execute(query_select_one, (categoria,))
         user = cursor.fetchone()
         return user