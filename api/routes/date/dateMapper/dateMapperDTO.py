from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.DateDTO import DateDTO, PostDateRequestDTO, DateResponseDTO, PatchDateRequestDTO, \
    UpdateDateRequestDTO


def mapPatchDateRequestDto(req: PatchDateRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchDateRequestDTO to a UpdateRequestDTO\n
    :param req: PatchDateRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    newFieldValue.append(UpdateFieldValue(field="date", value=req.date.date))
    return UpdateRequestDTO(
        table="date",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="date", value=req.identifier.date)
        ]
    )


def mapUpdateDateRequestDto(request: UpdateDateRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateDateRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateDateRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
        table="date",
        newFieldValue=[
            UpdateFieldValue(field="date", value=request.date.date),

        ],
        identifiers=[
            UpdateFieldValue(field="date", value=request.identifier.date)
        ]
    )


def mapInsertDateRequestDto(request: PostDateRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostDateRequestDTO to a InsertRequestDTO\n
    :param request: PostDateRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
        table="date",
        fieldValue=[
            FieldValue(field="date", value=request.date.date),

        ]
    )


def mapDeleteDateRequestDto(date: str) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param date:
    :return:
    """
    return DeleteItemRequestDTO(
        table="date",
        identifiers=[
            IdValue(field="date", value=str(date))
        ]
    )


