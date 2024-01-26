from fastapi import APIRouter, HTTPException
from logs import create_new_log
from db import dbConfig
from routes.dtoModel.DatasourceDTO import InsertRequestDTO
router = APIRouter()


async def insert(request: InsertRequestDTO):
    """
    description: insert a new item in the database \n

    :body:\n
        {
            "table": str,
            "field": [
                {
                    "field":str,
                    "value":str
                },
                ...
            ]
        }\n
    :return:\n
        {
            "table": str,
            "field": [
                {
                    "field":str,
                    "value":str
                },
                ...
            ]
        }\n
    """
    try:
        query = "INSERT INTO public." + request.table + " ("
        for field in request.fieldValue:
            query += field.field + ","
        query = query[:-1] + ") VALUES ("
        for field in request.fieldValue:
            if isinstance(field.value, str):
                query += "'" + field.value + "',"
            else:
                query += str(field.value) + ","
        query = query[:-1] + ");"
        conn = dbConfig.connect()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        await create_new_log("POST", request.table, "success")
        return {"message": "La ligne a bien été ajoutée à la table " + request.table, request.table: {"table": request.table, "field": request.fieldValue}, "statusCode": 200}
    except Exception as e:
        await create_new_log("POST", request.table, "fail")
        if str(e).__contains__("foreign key"):
            error_message = "Insertion échouée, dû à une erreur de clé étrangère"
        elif str(e).__contains__("invalid input syntax"):
            expected_type = str(e).split(" ")[5]
            error_message = "Erreur de type dans le remplissage des champs. Type attendu : " + expected_type[:-1]
        elif str(e).__contains__("date/time field value out of range"):
            error_message = "Format de date non valide"
        elif str(e).__contains__("violates unique constraint"):
            error_message = "Les clés primaires doivent être uniques"
        else:
            error_message = "Insertion échouée"
        raise HTTPException(400, error_message)

