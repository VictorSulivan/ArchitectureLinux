from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.UniteDTO import UniteDTO, PostUniteRequestDTO, UniteResponseDTO, PatchUniteRequestDTO, \
    UpdateUniteRequestDTO


def mapPatchUniteRequestDto(req: PatchUniteRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchUniteRequestDTO to a UpdateRequestDTO\n
    :param req: PatchUniteRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    newFieldValue.append(UpdateFieldValue(field="un", value=req.unite.un))
    return UpdateRequestDTO(
        table="un",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="un", value=req.identifier.un)
        ]
    )


def mapUpdateUniteRequestDto(request: UpdateUniteRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateUniteRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateUniteRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="un",
            newFieldValue=[
                UpdateFieldValue(field="un", value=request.unite.un),
                
            ],
            identifiers=[
                UpdateFieldValue(field="un", value=request.identifier.un)
            ]
        )


def mapInsertUniteRequestDto(request: PostUniteRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostUniteRequestDTO to a InsertRequestDTO\n
    :param request: PostUniteRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="un",
            fieldValue=[
                FieldValue(field="un", value=request.unite.un),
            ]
        )


def mapDeleteUniteRequestDto(un: str) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param un:
    :return:
    """
    return DeleteItemRequestDTO(
            table="un",
            identifiers=[
                IdValue(field="un", value=str(un))
            ]
        )


