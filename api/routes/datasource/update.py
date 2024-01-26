from fastapi import APIRouter, HTTPException
from logs import create_new_log
from db import dbConfig
from routes.dtoModel.DatasourceDTO import UpdateRequestDTO
router = APIRouter()


async def update(request: UpdateRequestDTO):
    """
    description: update all field of a line in the database \n

    :body:\n
        {
            "table": str,
            "newFieldValue": [
                {
                    "field":str,
                    "value":str
                },
                        {
                    "field":str,
                    "value":str
                },
                 ....
                    ],
            "identifiers": [
                {
                    "field":str,
                    "value":str
                },
                ...
            ]
        }\n
    :return:\n
        {
            "message" : "modification réussie",
            "code" : 200
        }\n
    """
    try:
        query = "UPDATE public." + request.table + " SET "
        for field in request.newFieldValue:
            if isinstance(field.value, str):
                query += field.field + "='" + field.value + "',"
            else:
                query += field.field + "=" + str(field.value) + ","
        query = query[:-1] + " WHERE "
        for identifier in request.identifiers:
            query += identifier.field + "='" + identifier.value + "' AND "
        query = query[:-4] + ";"
        conn = dbConfig.connect()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        if cur.rowcount == 0:
            await create_new_log("PUT/PATCH", request.table, "fail")
            raise HTTPException(400, "Aucune ligne ne correspond à ce ou ces identifiants")
        await create_new_log("PUT/PATCH", request.table, "success")
        cur.close()
        conn.close()
        return {"message": "modification réussie", "statusCode": 200}
    except Exception as e:
        await create_new_log("PUT/PATCH", request.table, "fail")
        if str(e).__contains__("foreign key"):
            error_message = "La modification a échoué, dû à une erreur de clé étrangère"
        elif str(e).__contains__("invalid input syntax"):
            expected_type = str(e).split(" ")[5]
            error_message = "Erreur de type dans le remplissage des champs. Type attendu : " + expected_type[:-1]
        elif str(e).__contains__("date/time field value out of range"):
            error_message = "Format de date non valide"
        elif str(e).__contains__("violates unique constraint"):
            error_message = "Les clés primaires doivent être uniques"
        elif str(e).__contains__("ce ou ces identifiants"):
            error_message = "Aucune ligne ne correspond à ce ou ces identifiants"
        else:
            error_message = "La modification a échoué"
        raise HTTPException(400, error_message)
        return {"message": error_message,
                "tableTry": request.table, "statusCode": 400}
