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


def execute_sql_comand_in_database(query):
    """Executa o query recebida por parametro com psycopg2"""

    conn, cursor = init_connection()

    cursor.execute(query)
    records = cursor.fetchall()

    conn.commit()
    conn.close()

    return records
