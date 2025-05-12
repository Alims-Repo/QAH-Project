import mysql.connector
from utils.json_reader import read_json
from utils.csv_reader import read_csv

creds = read_json('db_creds.json')
db_connection = mysql.connector.connect(
    host=creds['host'],
    user=creds['user'],
    password=creds['password'],
    database=creds['database']
)


def insert_data_sql(query,data:list):
    try:
        cursor = db_connection.cursor()
        cursor.executemany(query,data)
        print('Query executed successfully!!')
    except Exception as e:
        print(e.with_traceback())

    finally:
        db_connection.commit()
        cursor.close()
        db_connection.close()

def select_data_sql(query):
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        print('Query executed successfully!!')
    except Exception as e:
        print(e.with_traceback())
    finally:
        db_connection.commit()
        cursor.close()
        db_connection.close()


# for unit testing
# categories = [['All Categories'], ['Desktops'], ['PC'], ['Mac'], ['Laptops & Notebooks'], ['Macs'], ['Windows'], ['Components'], ['Mice and Trackballs'], ['Monitors'], ['test 1'], ['test 2'], ['Printers'], ['Scanners'], ['Web Cameras'], ['Tablets'], ['Software'], ['Phones & PDAs'], ['Cameras'], ['MP3 Players'], ['test 11'], ['test 12'], ['test 15'], ['test 16'], ['test 17'], ['test 18'], ['test 19'], ['test 20'], ['test 25'], ['test 21'], ['test 22'], ['test 23'], ['test 24'], ['test 4'], ['test 5'], ['test 6'], ['test 7'], ['test 8'], ['test 9']]
# query = '''
# insert into product_categories(category) values(%s);
# '''
# insert_data_sql(query,data=categories)


