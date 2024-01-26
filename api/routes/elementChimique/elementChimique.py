from logs import create_new_log
from routes import filter
from fastapi import APIRouter, Query, HTTPException
from routes.elementChimique.elementChimiqueMapper.elementChimiqueMapperDTO import mapPatchElementChimiqueRequestDto, mapInsertElementChimiqueRequestDto, \
    mapDeleteElementChimiqueRequestDto, mapUpdateElementChimiqueRequestDto
from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.ElementChimiqueDTO import ElementChimiqueDTO, PostElementChimiqueRequestDTO, PatchElementChimiqueRequestDTO, \
    UpdateElementChimiqueRequestDTO
from routes.datasource.delete import delete
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.update import update
router = APIRouter()


@router.post("/element_chimique", tags=["Elements Chimiques"])
async def insert_element_chimique(request: PostElementChimiqueRequestDTO):
    """
    description: insert a new chemical element item in the database\n

    :body:\n
        {
            "elementChimique": {
                "surface": str,
                "nom_parcelle": str,
                "coordonnees": str,
            }
        }\n
    :return:\n
        {
            "message": "L'élément chimique a bien été créée",
            "parcelle": {
                "surface": str,
                "nom_parcelle": str,
                "coordonnees": str,
            }
        }\n
    """
    try:
        return await insert(mapInsertElementChimiqueRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "elements_chimiques", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.get("/element_chimique", tags=["Elements Chimiques"])
async def get_element_chimique(code_element: str | None = None, un: str | None = None,
                               libelle_element: str | None = None, fields: str | None = None,
                               order: str | None = None, page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: get all elements chimiques items in the database\n
    query parameters: \n
        code_element: str or None
        un: str or None
        libelle_element: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:\n
        {
        "table": "elements_chimiques",
        "fieldValue": [
            {
                "code_element": str,
                "un": str,
                "libelle_element": str,
            },
            ...
        ]
    }\n
    """
    try:
        table_fields = ["code_element", "un", "libelle_element"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="elements_chimiques",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )
        return await select(req, page, size)
    except Exception as e:
        await create_new_log("GET", "elements_chimiques", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.delete("/element_chimique", tags=["Elements Chimiques"])
async def delete_element_chimique(code_element: str):
    """
    description: delete a element chimique item in the database\n
    :param id:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeleteElementChimiqueRequestDto(code_element))
    except Exception as e:
        await create_new_log("DELETE", "elements_chimiques", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.put("/element_chimique", tags=["Elements Chimiques"])
async def update_element_chimique(request: UpdateElementChimiqueRequestDTO):
    """
    description: update all field of a element chimique item in the database\n
    :param request:

    :body:\n
        {
            "parcelle": {
                "code_element": str,
                "un": str,
                "libelle_element": str,
            }
        }\n

    :return:\n
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapUpdateElementChimiqueRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "elements_chimiques", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


@router.patch("/element_chimique", tags=["Elements Chimiques"])
async def patch_element_chimique(request: PatchElementChimiqueRequestDTO):
    """
    description: update some field of a element chimique item in the database\n

    :param request:

    :body:\n
        {
            "element_chimique": {
                "code_element": str,
                "un": str,
                and or
                "libelle_element": str,
            }
        }\n
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchElementChimiqueRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "elements_chimiques", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])