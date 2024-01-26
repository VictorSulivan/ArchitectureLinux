from routes import filter
from fastapi import APIRouter, Query, HTTPException
from routes.posseder.possederMapper.possederMapperDTO import mapPatchPossederRequestDto, mapInsertPossederRequestDto, \
    mapDeletePossederRequestDto, mapUpdatePossederRequestDto
from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.PossederDTO import PossederDTO, PostPossederRequestDTO, PossederResponseDTO, PatchPossederRequestDTO, \
    UpdatePossederRequestDTO
from routes.datasource.delete import delete
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.update import update
from logs import create_new_log
router = APIRouter()


@router.post("/posseder", tags=["Posseder"])
async def insert_posseder(request: PostPossederRequestDTO):
    """
    description: insert a new posseder item in the database\n

    :body:\n
        {
            "posseder": {
                "id_engrais": str,
                "code_element": str,
                "valeur": str,
            }
        }\n
    :return:\n
        {
            "message": "Le posseder a bien été créée",
            "posseder": {
                "id_engrais": str,
                "code_element": str,
                "valeur": str,
            }
        }\n
    """
    try:
        return await insert(mapInsertPossederRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "posseder", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.get("/posseder", tags=["Posseder"])
async def get_posseder(id_engrais: int | None = None, code_element: str | None = None,
                       valeur: str | None = None, fields: str | None = None,
                       order: str | None = None, page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: get all posseder item in the database\n
    query parameters: \n
        id_engrais: int or None
        code_element: str or None
        valeur: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:\n
        {
        "table": "posseder",
        "fieldValue": [
            {
                "id_engrais": str,
                "code_element": str,
                "valeur": str,
            },
            ...
        ]
    }\n
    """
    try:
        table_fields = ["id_engrais", "code_element", "valeur"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="posseder",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )
        return await select(req, page, size)
    except Exception as e:
        await create_new_log("GET", "posseder", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.delete("/posseder", tags=["Posseder"])
async def delete_posseder(id_engrais: int, code_element: str):
    """
    description: delete a posseder item in the database\n
    :param engrais:\n
    :param element:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeletePossederRequestDto(id_engrais, code_element))
    except Exception as e:
        await create_new_log("DELETE", "posseder", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.put("/posseder", tags=["Posseder"])
async def update_posseder(request: UpdatePossederRequestDTO):
    """
    description: update all field of a posseder item in the database\n
    :param request:

    :body:\n
        {
            "posseder": {
                "id_engrais": str,
                "code_element": str,
                "valeur": str,
            },
            "identifiers": {
                "id_engrais": str,
                "code_element": str,
            }
        }\n

    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapUpdatePossederRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "posseder", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.patch("/posseder", tags=["Posseder"])
async def patch_posseder(request: PatchPossederRequestDTO):
    """
    description: update some field of a posseder item in the database\n

    :param request:

    :body:\n
        {
            "posseder": {
                "id_engrais": str,
                and or
                "code_element": str,
                and or
                "valeur": str,
            },
            "identifiers": {
                "id_engrais": str,
                "code_element": str,
            }
        }\n
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchPossederRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "posseder", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])
