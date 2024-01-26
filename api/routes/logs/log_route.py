from fastapi import APIRouter
from routes.dtoModel.DatasourceDTO import OrderDTO, SelectRequestDTO, ConditionDTO
from routes.datasource.select import select
from logs import create_new_log

router = APIRouter()


@router.get("/logs")
async def get_logs(method: str, table: str):
    """
    Returns the number of requests made to a certain endpoint
    """
    try:
        if method.upper() not in ["POST", "GET", "PUT", "PATCH", "DELETE"]:
            raise Exception("invalid method")
        if method.upper() == "PUT" or method.upper() == "PATCH":
            method = "PUT/PATCH"
        req = SelectRequestDTO(
            table="logs",
            selectedFields=["*"],
            conditions=[ConditionDTO(field="method", value=method.upper()), ConditionDTO(field="table", value=table)],
            order=OrderDTO(field="", type=""),
            id=""
        )
        response = await select(req, -1, -1)
        return {"message": f"The method '{method}' was used {str(len(response['fieldValue']))} times on the table '{table}'"}
    except Exception as e:
        await create_new_log("GET", "logs", "fail")
        return {"message": str(e), "status": 400}
