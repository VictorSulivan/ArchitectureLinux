from logs import create_new_log
from routes import filter
from fastapi import APIRouter, Query, HTTPException
from routes.parcelle.parcelleMapper.parcelleMapperDTO import mapPatchParcelleRequestDto, mapInsertParcelleRequestDto, \
    mapDeleteParcelleRequestDto, mapUpdateParcelleRequestDto
from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO, ConditionDTO
from routes.dtoModel.ParcelleDTO import ParcelleDTO, PostParcelleRequestDTO, ParcelleResponseDTO, PatchParcelleRequestDTO, \
    UpdateParcelleRequestDTO
from routes.datasource.delete import delete
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.update import update
router = APIRouter()


@router.post("/parcelle", tags=["Parcelle"])
async def insert_parcelle(request: PostParcelleRequestDTO):
    """
    description: insert a new parcelle item in the database\n

    :body:\n
        {
            "parcelle": {
                "surface": str,
                "nom_parcelle": str,
                "coordonnees": str,
            }
        }\n
    :return:\n
        {
            "message": "La parcelle a bien été créée",
            "parcelle": {
                "surface": str,
                "nom_parcelle": str,
                "coordonnees": str,
            }
        }\n
    """
    try:
        return await insert(mapInsertParcelleRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "parcelle", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.get("/parcelle", tags=["Parcelle"])
async def get_parcelle(no_parcelle: int | None = None, surface: str | None = None,
                       nom_parcelle: str | None = None, coordonnees: str | None = None,
                       fields: str | None = None, order: str | None = None,
                       page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: get all parcelle item in the database\n
    query parameters: \n
        no_parcelle: int or None
        surface: str or None
        nom_parcelle: str or None
        coordonnees: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:\n
        {
        "table": "parcelle",
        "fieldValue": [
            {
                "no_parcelle": int,
                "surface": int,
                "nom_parcelle": str,
                "coordonnees": str,
            },
            ...
        ]
    }\n
    """
    try:
        table_fields = ["no_parcelle", "surface", "nom_parcelle", "coordonnees"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="parcelle",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )
        return await select(req, page, size)
    except Exception as e:
        await create_new_log("GET", "parcelle", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.delete("/parcelle", tags=["Parcelle"])
async def delete_parcelle(no_parcelle: int):
    """
    description: delete a parcelle item in the database\n
    :param id:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeleteParcelleRequestDto(no_parcelle))
    except Exception as e:
        await create_new_log("DELETE", "parcelle", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.put("/parcelle", tags=["Parcelle"])
async def update_parcelle(request: UpdateParcelleRequestDTO):
    """
    description: update all field of a parcelle item in the database\n
    :param request:

    :body:\n
        {
            "parcelle": {
                "no_parcelle": str,
                "surface": str,
                "nom_parcelle": str,
                "coordonnees": str,
            }
        }\n

    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapUpdateParcelleRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "parcelle", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.patch("/parcelle", tags=["Parcelle"])
async def patch_parcelle(request: PatchParcelleRequestDTO):
    """
    description: update some field of a parcelle item in the database\n

    :param request:

    :body:\n
        {
            "parcelle": {
                "no_parcelle": str,
                "surface": str,
                and or
                "nom_parcelle": str,
                and or
                "coordonnees": str,
            }
        }\n
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchParcelleRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "parcelle", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])