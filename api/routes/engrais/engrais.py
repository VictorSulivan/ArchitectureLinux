from logs import create_new_log
from routes import filter
from fastapi import APIRouter, Query, HTTPException
from routes.engrais.engraisMapper.engraisMapperDTO import mapPatchEngraisRequestDto, mapInsertEngraisRequestDto, \
    mapDeleteEngraisRequestDto, mapUpdateEngraisRequestDto
from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.EngraisDTO import EngraisDTO, PostEngraisRequestDTO, EngraisResponseDTO, PatchEngraisRequestDTO, \
    UpdateEngraisRequestDTO
from routes.datasource.delete import delete
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.update import update
router = APIRouter()


@router.post("/engrais", tags=["Engrais"])
async def engrais(request: PostEngraisRequestDTO):
    """
    description: insert a new engrais item in the database\n

    :body:\n
        {
            "engrais": {
                "un": str,
                "nom_engrais": str
            }
        }\n
    :return:\n
        {
            "message": "L'engrais a bien été créée",
            "engrais": {
                "un": str,
                "nom_engrais": str
            }
        }\n
    """
    try:
        return await insert(mapInsertEngraisRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "engrais", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.get("/engrais", tags=["Engrais"])
async def get_engrais(id_engrais: int | None = None, un: str | None = None,
                      nom_engrais: str | None = None, fields: str | None = None,
                      order: str | None = None, page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: get all engrais item in the database\n
    query parameters: \n
        id_engrais: int or None
        un: str or None
        nom_engrais: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:\n
        {
        "table": "engrais",
        "fieldValue": [
            {
                "id_engrais": int,
                "un": str,
                "nom_engrais": str
            },
            ...
        ]
    }\n
    """
    try:
        table_fields = ["id_engrais", "un", "nom_engrais"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="engrais",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )
        return await select(req, page, size)
    except Exception as e:
        await create_new_log("GET", "engrais", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.delete("/engrais", tags=["Engrais"])
async def delete_engrais(id_engrais: int):
    """
    description: delete a engrais item in the database\n
    :param id_engrais:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeleteEngraisRequestDto(id_engrais))
    except Exception as e:
        await create_new_log("DELETE", "engrais", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.put("/engrais", tags=["Engrais"])
async def update_engrais(request: UpdateEngraisRequestDTO):
    """
    description: update all field of a engrais item in the database\n
    :param request:

    :body:\n
        {
            "engrais": {
                "id_engrais": int,
                "un": str,
                "nom_engrais": str
            }
        }\n

    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapUpdateEngraisRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "engrais", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.patch("/engrais", tags=["Engrais"])
async def patch_engrais(request: PatchEngraisRequestDTO):
    """
    description: update some field of a engrais item in the database\n

    :param request:

    :body:\n
        {
            "engrais": {
                "id_engrais": int,
                "un": str,
                and or
                "nom_engrais": str
            }
        }\n
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchEngraisRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "engrais", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])
