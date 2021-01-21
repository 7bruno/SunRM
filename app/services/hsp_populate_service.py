import csv

import psycopg2
from environs import Env


def init_connection():
    """inicia uma conneção apartir do database no .env"""

    env = Env()
    env.read_env()

    dbname = env.str('DATABASE_NAME')
    user = env.str('DATABASE_USER')
    password = env.str('DATABASE_PASSWORD')

    conn = psycopg2.connect(
        f"""dbname={dbname} user={user} password={password} host=localhost port=5432"""
    )

    cursor = conn.cursor()
    return conn, cursor


def hsp_readers(csv_string_name):
    with open(csv_string_name, 'r') as file:

        reader = csv.DictReader(
            file
        )
        for hsp in reader:
            new_hsp = {}
            new_hsp.update({
                "city": hsp["NAME"],
                "uf": hsp["STATE"],
                "md_anual": hsp["ANNUAL"],
                "lon": hsp["LON"],
                "lat": hsp["LAT"]
            })

            yield new_hsp


def populating_hsp():

    conn, cursor = init_connection()

    for data in hsp_readers("hsp_data_2017.csv"):

        cursor.execute("INSERT INTO hsp (city,uf,md_anual,lon,lat) VALUES(%s,%s,%s,%s,%s)",
                       (data["city"], data["uf"], data["md_anual"], data["lon"], data["lat"]))

        conn.commit()
    cursor.close()
    conn.close()


populating_hsp()
