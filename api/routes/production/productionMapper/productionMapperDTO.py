from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.ProductionDTO import PostProductionRequestDTO, UpdateProductionRequestDTO, \
    PatchProductionRequestDTO


def mapInsertProductionRequestDto(request: PostProductionRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostProductionRequestDTO to a InsertRequestDTO\n
    :param request: PostProductionRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="production",
            fieldValue=[
                FieldValue(field="un", value=request.production.un),
                FieldValue(field="nom_production", value=request.production.nom_production),
            ]
        )


def mapUpdateProductionRequestDto(request: UpdateProductionRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateCultureRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateCultureRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="production",
            newFieldValue=[
                UpdateFieldValue(field="un", value=request.production.un),
                UpdateFieldValue(field="nom_production", value=request.production.nom_production),
            ],
            identifiers=[
                UpdateFieldValue(field="code_production", value=request.production.code_production)
            ]
        )


def mapPatchProductionRequestDto(req: PatchProductionRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchCultureRequestDTO to a UpdateRequestDTO\n
    :param req: PatchCultureRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    if req.production.un is not None:
        newFieldValue.append(UpdateFieldValue(field="un", value=req.production.un))
    if req.production.nom_production is not None:
        newFieldValue.append(UpdateFieldValue(field="nom_production", value=req.production.nom_production))
    return UpdateRequestDTO(
        table="production",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="code_production", value=req.production.code_production)
        ]
    )


def mapDeleteProductionRequestDto(code_production: int) -> DeleteItemRequestDTO:
    """
    description: map a CultureDTO to a DeleteItemRequestDTO\n
    :param code_production: CultureDTO
    :return: DeleteItemRequestDTO
    """
    return DeleteItemRequestDTO(
        table="production",
        identifiers=[
            IdValue(field="code_production", value=str(code_production))
        ]
    )