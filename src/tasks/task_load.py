from config import config
from  mysql import connector
from prefect import task

@task(name="Carga de info a BD")
def task_load_food(food_data):
    print(food_data)
    with connector.connect(**config.MYSQL_CONFIG) as db:
        with db.cursor() as cursor:
            query_insert ="""
            insert into food(categoria,origen,foto,cantidad)
            values(%s,%s,%s,%s)   
            """
            cursor.execute(query_insert, food_data)
            db.commit()