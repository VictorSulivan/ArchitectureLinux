from fastapi import APIRouter, HTTPException
from logs import create_new_log
from db import dbConfig
from routes.dtoModel.DatasourceDTO import DeleteItemRequestDTO
router = APIRouter()


async def delete(request: DeleteItemRequestDTO):
    """
    Function to delete an entity from the database
    """
    try:
        query = "DELETE FROM public."
        query += request.table + " WHERE "
        for identifier in request.identifiers:
            query += identifier.field + "='" + str(identifier.value) + "' AND "
        query = query[:-4] + ";"
        conn = dbConfig.connect()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        if cur.rowcount == 0:
            await create_new_log("DELETE", request.table, "fail")
            raise HTTPException(400, "Aucune ligne ne correspond à ce ou ces identifiants")
        await create_new_log("DELETE", request.table, "success")
        return {"message": "La suppression a bien été effectuée", "statusCode": 200}
    except Exception as e:
        await create_new_log("DELETE", request.table, "fail")
        if str(e).__contains__("foreign key"):
            error_message = "La suppression a échoué, dû à une erreur de clé étrangère"
        elif str(e).__contains__("ce ou ces identifiants"):
            error_message = "Aucune ligne ne correspond à ce ou ces identifiants"
        else:
            error_message = "La suppression a échoué"
        raise HTTPException(400, error_message)
        return {"message": error_message, "statusCode": 400}
