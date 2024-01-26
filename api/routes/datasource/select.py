import psycopg2
from logs import create_new_log
from fastapi import APIRouter, HTTPException
from db import dbConfig
from routes.dtoModel.DatasourceDTO import SelectRequestDTO, OrderDTO
router = APIRouter()


async def select(request: SelectRequestDTO, page: int, size: int):
    """
    description: select a new item in the database \n

    :body:\n
    {
        "table": str,
        "fieldValue": [str,str,...],
        "order": {
            "field": str,
            "type": "asc" ou "desc"
        },
        "id": str,
    }\n
    :return:\n
        {
            "table": str,
            "fieldValue": [
                {
                    "field": "value",
                    ...
                },
                ...
            ]
        }\n
    """
    try:
        query = "SELECT "
        for field in request.selectedFields:
            query += field + ","
        query = query[:-1] + " FROM public." + request.table
        """if request.id != "":
            query += " WHERE id = " + request.id"""
        if request.conditions != []:
            query += " WHERE "
            for condition in request.conditions:
                query += '"'+condition.field + "\"='" + condition.value + "' AND "
            query = query[:-4]
        if request.order.field != "":
            query += " ORDER BY " + request.order.field + " " + request.order.type

        # Do pagination if page and size are not -1
        if page != -1 and size != -1:
            offset = (page - 1) * size
            query += f" LIMIT {size} OFFSET {offset};"

        query += ";"
        conn = dbConfig.connect()
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        data = []
        columns = cur.description
        for row in rows:
            row_data = {}
            for i, name in enumerate(row):
                row_data[columns[i][0]] = name
            data.append(row_data)
        await create_new_log("GET", request.table, "success")
        return {"table": request.table, "fieldValue": data}
    except (Exception, psycopg2.DatabaseError) as error:
        await create_new_log("GET", request.table, "fail")
        raise HTTPException(400, "La sélection a échoué")
