from logs import create_new_log
from routes import filter
from fastapi import APIRouter, Query, HTTPException
from routes.dtoModel.DatasourceDTO import SelectRequestDTO, OrderDTO
from routes.dtoModel.ProductionDTO import ProductionDTO, PostProductionRequestDTO, PatchProductionRequestDTO, \
    PatchProductionDTO, UpdateProductionRequestDTO, UpdateProductionDTO
from routes.datasource.delete import delete
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.update import update
from routes.production.productionMapper.productionMapperDTO import mapPatchProductionRequestDto, \
    mapUpdateProductionRequestDto, mapDeleteProductionRequestDto, mapInsertProductionRequestDto
router = APIRouter()


@router.post("/production", tags=["Production"])
async def post_production(request: PostProductionRequestDTO):
    """
    description: insert a new production item in the database\n

    :body:\n
        {
            "production": {
                "un": str,
                "nom_production": str
            }
        }\n
    :return:\n
        {
            "message": "La production a bien été créée",
            "production": {
                "un": str,
                "nom_production": str
            }
        }\n
    """
    try:
        return await insert(mapInsertProductionRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "production", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.get("/production", tags=["Production"])
async def get_production(code_production: int | None = None, un: str | None = None,
                       nom_production: str | None = None, fields: str | None = None,
                       order: str | None = None, page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: get all production item in the database\n
    query parameters: \n
        code_production: int or None
        un: str or None
        nom_production: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:\n
        {
        "table": "production",
        "fieldValue": [
            {
                "code_production": int,
                "un": str,
                "nom_production": str
            },
        ]
    }\n
    """
    try:
        table_fields = ["code_production", "un", "nom_production"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="production",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )
        return await select(req, page, size)
    except Exception as e:
        await create_new_log("GET", "production", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.delete("/production", tags=["Production"])
async def delete_production(code_production: int):
    """
    description: delete a production item in the database\n
    :param code_production: id of the production item\n
    :return:\n
        {
            "message": "La production a bien été supprimée",
            "status": 200
        }\n
    """
    try:
        return await delete(mapDeleteProductionRequestDto(code_production))
    except Exception as e:
        await create_new_log("DELETE", "production", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.put("/production", tags=["Production"])
async def update_production(request: UpdateProductionRequestDTO):
    """
    description: update a production item in the database\n

    :body:\n
        {
            "production": {
                "code_production": int,
                "un": str,
                "nom_production": str
            }
        }\n
    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapUpdateProductionRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "production", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.patch("/production", tags=["Production"])
async def patch_production(request: PatchProductionRequestDTO):
    """
    description: update a production item in the database\n

    :body:\n
        {
            "production": {
                "code_production": int,
                "un": str,
                and or
                "nom_production": str
            }
        }\n
    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchProductionRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "production", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])
