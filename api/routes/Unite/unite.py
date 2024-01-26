from fastapi import APIRouter, Query, HTTPException
from logs import create_new_log
from fastapi.responses import JSONResponse
from routes import filter
from routes.Unite.uniteMapper.uniteMapperDTO import mapInsertUniteRequestDto, mapDeleteUniteRequestDto, \
    mapUpdateUniteRequestDto, mapPatchUniteRequestDto
from routes.dtoModel.DatasourceDTO import SelectRequestDTO, FieldValue, OrderDTO, UpdateRequestDTO
from routes.dtoModel.UniteDTO import UniteDTO, PostUniteRequestDTO, UniteResponseDTO, PatchUniteRequestDTO, \
    UpdateUniteRequestDTO
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.delete import delete
from routes.datasource.update import update

router = APIRouter()


########## POST ##########
@router.post("/unite", tags=["Unite"])
async def unite(request: PostUniteRequestDTO):

    """description: insert a new unite in the database
            {
            "unite":
                {
                    "un" : str
                }
            }
            :return:
            "{
            "message"": ""unite bien ajoutee !",
            "unite":
                {
                    "un" : str
                }
        }
    """

    try:
        return await insert(mapInsertUniteRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "unite", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


########## GET ##########
@router.get("/unite", tags=["Unite"])
async def get_unite(un: str | None = None, fields: str | None = None, order: str | None = None,
                    page: int = Query(default=-1), size: int = Query(default=-1)):
    """description: select all unite in the database\n
    query parameters: \n
        un: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:
    {
    "message": "unite bien selectionnée !",
    "unite": [
        {
            "un": str
        },
        ...
    ]
}"""

    try:
        table_fields = ["un"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="un",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )

        return await select(req, page, size)

    except Exception as e:
        await create_new_log("GET", "unite", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


########## DELETE ##########
@router.delete("/unite", tags=["Unite"])
async def delete_unite(un: str):
    """
    description: delete a unite item in the database\n
    :param un:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeleteUniteRequestDto(un))
    except Exception as e:
        await create_new_log("DELETE", "unite", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '")+3:-2])


########## PUT ##########
@router.put("/unite", tags=["Unite"])
async def update_unite(request: UpdateUniteRequestDTO):
    """
    description: update all field of a unite item in the database\n
    :param request:
    {
    "unite":
        {
            "un" : "TestPUTcollection"
        },
    "identifier":
        {
            "un": "plouf"
        }
    }
    :return:
    {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n

    """
    try:
        return await update(mapUpdateUniteRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "unite", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


########## PATCH ##########
@router.patch("/unite", tags=["Unite"])
async def patch_unite(request: PatchUniteRequestDTO):
    """
    description: update some field of a unite item in the database\n

    :param request:
    {
    "unite":
        {
            "un" : "TestPatchcollection"
        },
    "identifier":
        {
            "un": "osekour"
        }
}
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchUniteRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "unite", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])
