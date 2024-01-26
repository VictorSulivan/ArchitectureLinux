from datetime import datetime
from db import dbConfig


async def create_new_log(method, table, status):
    file = open("logs.txt", "a")
    file.write(f"Méthode : {method} - ")
    file.write(f"Table : {table} - ")
    file.write(f"Date : {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')} - ")
    file.write(f"Statut : {str(status)}\n")
    file.close()
    conn = dbConfig.connect()
    cur = conn.cursor()
    cur.execute(f'INSERT INTO public.logs ("method", "table", "status", "timestamp") VALUES(%s, %s, %s, %s)', (method, table, status, datetime.now()))
    conn.commit()
    conn.close()
