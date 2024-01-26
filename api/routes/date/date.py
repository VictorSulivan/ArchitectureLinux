from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse
from logs import create_new_log
from routes import filter
from routes.date.dateMapper.dateMapperDTO import mapInsertDateRequestDto, mapDeleteDateRequestDto, \
    mapUpdateDateRequestDto, mapPatchDateRequestDto
from routes.dtoModel.DatasourceDTO import SelectRequestDTO, FieldValue, OrderDTO, UpdateRequestDTO
from routes.dtoModel.DateDTO import DateDTO, PostDateRequestDTO, DateResponseDTO, PatchDateRequestDTO, \
    UpdateDateRequestDTO
from routes.datasource.insert import insert
from routes.datasource.select import select
from routes.datasource.delete import delete
from routes.datasource.update import update

router = APIRouter()


########## POST ##########
@router.post("/date", tags=["Date"])
async def date(request: PostDateRequestDTO):

    """description: insert a new date in the database
    {
        "date":
        {
            "date" : date
        }
    }
    :return:
    {
    "message": "date bien ajoutée !",
    "date":
        {
            "date" : date
        }
    }
    """

    try:
        return await insert(mapInsertDateRequestDto(request))
    except Exception as e:
        await create_new_log("POST", "date", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


########## GET ##########
@router.get("/date", tags=["Date"])
async def get_date(date: str | None = None, fields: str | None = None, order: str | None = None, page: int = Query(default=-1), size: int = Query(default=-1)):
    """
    description: select all date in the database\n
    query parameters:\n
        date: str or None
        fields: list of fields separated by comma
        order: field followed by + or - or nothing
        page: int or None
        size: int or None
    :return:
    {
    "date":
        {
            "date" : date
        }
    }
}"""

    try:
        table_fields = ["date"]
        filters = filter.select_filter(locals().values().mapping.items(), fields, order, table_fields)
        req = SelectRequestDTO(
            table="date",
            selectedFields=filters[0],
            conditions=filters[1],
            order=filters[2],
            id=""
        )

        return await select(req, page, size)

    except Exception as e:
        await create_new_log("GET", "date", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


########## DELETE ##########
@router.delete("/date", tags=["Date"])
async def delete_date(date: str):
    """
    description: delete a date item in the database\n
    :param id:\n
    :return:\n
    {
        "message": "La suppression a bien été effectuée",
        "status": 200
    }\n
    """
    try:
        return await delete(mapDeleteDateRequestDto(date))
    except Exception as e:
        await create_new_log("DELETE", "date", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


########## PUT ##########
@router.put("/date", tags=["Date"])
async def update_date(request: UpdateDateRequestDTO):
    """
    description: update all field of a date item in the database\n
    :param request:
    {
    "date":
        {
            "date" : "2023-03-26"
        },
    "identifier":
        {
            "date": "2023-03-11"
        }
    }
    :return:
    {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n

    """
    try:
        return await update(mapUpdateDateRequestDto(request))
    except Exception as e:
        await create_new_log("PUT", "date", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])


########## PATCH ##########
@router.patch("/date", tags=["Date"])
async def patch_date(request: PatchDateRequestDTO):
    """
    description: update some field of a date item in the database\n

    :param request:
    {
    "date":
        {
            "date" : "2023-03-03"
        },
    "identifier":
        {
            "date": "2023-03-26"
        }
    }
    :return:
        {
            "message": "La modification a bien été effectuée",
            "status": 200
        }\n
    """
    try:
        return await update(mapPatchDateRequestDto(request))
    except Exception as e:
        await create_new_log("PATCH", "date", "fail")
        raise HTTPException(400, str(e)[str(e).index(", '") + 3:-2])
