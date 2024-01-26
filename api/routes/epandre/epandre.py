from logs import create_new_log
from routes import filter
from fastapi import APIRouter, Query, HTTPException
from routes.epandre.epandreMapper.epandreMapperDTO import mapPatchEpandreRequestDto, mapInsertEpandreRequestDto, \
    mapDeleteEpandreRequestDto, mapUpdateEpandreRequestDto
from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.EpandreDTO import EpandreDTO, PostEpandreRequestDTO, EpandreResponseDTO, PatchEpandreRequestDTO, \
    UpdateEpandreRequestDTO
from routes.datasource.delete import delete
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.update import update
router = APIRouter()


@router.post("/epandre", tags=["Epandre"])
async def insert_epandre(request: PostEpandreRequestDTO):
    """
    description: insert a new epandre item in the database\n

    :body:\n
        {
            "epandre": {
                "id_engrais": str,
                "no_parcelle": str,
                "date": str,
                "qte_epandue": str,
            }
        }\n
    :return:\n
        {
            "message": "L'epandre a bien été créée",
            "epandre": {
                "id_engrais": str,
                "no_parcelle": str,
                "date": str,
                "qte_epandue": str,
            }
        }\n
    """
    try:
        return await insert(mapInsertEpandreRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "epandre", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.get("/epandre", tags=["Epandre"])
async def get_epandre(id_engrais: int | None = None, no_parcelle: str | None = None, date: str | None = None,
                      qte_epandue: str | None = None, fields: str | None = None,
                      order: str | None = None, page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: get all epandre item in the database\n
    query parameters: \n
        id_engrais: int or None
        no_parcelle: str or None
        date: str or None
        qte_epandue: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:\n
        {
        "table": "epandre",
        "fieldValue": [
            {
                "id_engrais": int,
                "no_parcelle": int,
                "date": str,
                "qte_epandue": str,
            },
            ...
        ]
    }\n
    """
    try:
        table_fields = ["id_engrais", "no_parcelle", "date", "qte_epandue"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="epandre",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )
        return await select(req, page, size)
    except Exception as e:
        await create_new_log("GET", "epandre", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.delete("/epandre", tags=["Epandre"])
async def delete_epandre(id_engrais: int, no_parcelle: int, date: str):
    """
    description: delete a epandre item in the database\n
    :param engrais:\n
    :param parcelle:\n
    :param date:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeleteEpandreRequestDto(id_engrais, no_parcelle, date))
    except Exception as e:
        await create_new_log("DELETE", "epandre", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.put("/epandre", tags=["Epandre"])
async def update_epandre(request: UpdateEpandreRequestDTO):
    """
    description: update all field of a epandre item in the database\n
    :param request:

    :body:\n
        {
            "epandre": {
                "id_engrais": str,
                "no_parcelle": str,
                "date": str,
                "qte_epandue": str,
            },
            "identifiers": {
                "id_engrais": str,
                "no_parcelle": str,
                "date": str,
            }
        }\n

    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapUpdateEpandreRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "epandre", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.patch("/epandre", tags=["Epandre"])
async def patch_epandre(request: PatchEpandreRequestDTO):
    """
    description: update some field of a epandre item in the database\n

    :param request:

    :body:\n
        {
            "epandre": {
                "id_engrais": str,
                and or
                "no_parcelle": str,
                and or
                "date": str,
                and or
                "qte_epandue": str,
            },
            "identifiers": {
                "id_engrais": str,
                "no_parcelle": str,
                "date": str,
            }
        }\n
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchEpandreRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "epandre", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])