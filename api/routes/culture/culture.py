from fastapi import APIRouter, HTTPException
from logs import create_new_log
from routes import filter
from fastapi import APIRouter, Query
from routes.culture.cultureMapper.cultureMapper import mapPatchCultureRequestDto, mapInsertCultureRequestDto, \
    mapDeleteCultureRequestDto, mapUpdateCultureRequestDto
from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.CultureDTO import CultureDTO, PostCultureRequestDTO, CultureResponseDTO, PatchCultureRequestDTO, \
    UpdateCultureRequestDTO
from routes.datasource.delete import delete
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.update import update
router = APIRouter()


@router.post("/culture", tags=["Culture"])
async def culture(request: PostCultureRequestDTO):
    """
    description: insert a new culture item in the database\n

    :body:\n
        {
            "culture": {
                "no_parcelle": str,
                "code_production": str,
                "date_debut": str,
                "date_fin": str,
                "qte_recoltee": str
            }
        }\n
    :return:\n
        {
            "message": "La culture a bien été créée",
            "culture": {
                "no_parcelle": str,
                "code_production": str,
                "date_debut": str,
                "date_fin": str,
                "qte_recoltee": str
            }
        }\n
    """
    try:
        return  await insert(mapInsertCultureRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "culture", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.get("/culture", tags=["Culture"])
async def get_culture(identifiant_culture: int | None = None, no_parcelle: int | None = None,
                      code_production: int | None = None, date_debut: str | None = None,
                      date_fin: str | None = None, qte_recoltee: str | None = None,
                      fields: str | None = None, order: str | None = None,
                      page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: get all culture item in the database\n
    query parameters: \n
        identifiant_culture: int or None
        no_parcelle: int or None
        code_production: int or None
        date_debut: str or None
        date_fin: str or None
        qte_recoltee: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:\n
        {
        "table": "culture",
        "fieldValue": [
            {
                "identifiant_culture": int,
                "no_parcelle": 1,
                "code_production": 1,
                "date_debut": str date,
                "date_fin": str date,
                "qte_recoltee": 1
            },
            ...
        ]
    }\n
    """
    try:
        table_fields = ["identifiant_culture", "no_parcelle", "code_production", "date_debut", "date_fin", "qte_recoltee"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="culture",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )
        return await select(req, page, size)
    except Exception as e:
        await create_new_log("GET", "culture", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.delete("/culture", tags=["Culture"])
async def delete_culture(identifiant_culture: int):
    """
    description: delete a culture item in the database\n
    :param identifiant_culture:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeleteCultureRequestDto(identifiant_culture))
    except Exception as e:
        await create_new_log("DELETE", "culture", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.put("/culture", tags=["Culture"])
async def update_culture(request: UpdateCultureRequestDTO):
    """
    description: update all field of a culture item in the database\n
    :param request:

    :body:\n
        {
            "culture": {
                "identifiant_culture": int,
                "no_parcelle": str,
                "code_production": str,
                "date_debut": str,
                "date_fin": str,
                "qte_recoltee": str
            }
        }\n

    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapUpdateCultureRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "culture", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.patch("/culture", tags=["Culture"])
async def patch_culture(request: PatchCultureRequestDTO):
    """
    description: update some field of a culture item in the database\n

    :param request:

    :body:\n
        {
            "culture": {
                "identifiant_culture": int,
                "no_parcelle": str,
                and or
                "code_production": str,
                and or
                "date_debut": str,
                and or
                "date_fin": str,
                and or
                "qte_recoltee": str
            }
        }\n
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchCultureRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "culture", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])