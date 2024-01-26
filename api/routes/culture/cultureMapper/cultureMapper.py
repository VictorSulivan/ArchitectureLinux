from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.CultureDTO import CultureDTO, PostCultureRequestDTO, CultureResponseDTO, PatchCultureRequestDTO, \
    UpdateCultureRequestDTO


def mapPatchCultureRequestDto(req: PatchCultureRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchCultureRequestDTO to a UpdateRequestDTO\n
    :param req: PatchCultureRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    if req.culture.no_parcelle is not None:
        newFieldValue.append(UpdateFieldValue(field="no_parcelle", value=req.culture.no_parcelle))
    if req.culture.code_production is not None:
        newFieldValue.append(UpdateFieldValue(field="code_production", value=req.culture.code_production))
    if req.culture.date_debut is not None:
        newFieldValue.append(UpdateFieldValue(field="date_debut", value=req.culture.date_debut))
    if req.culture.date_fin is not None:
        newFieldValue.append(UpdateFieldValue(field="date_fin", value=req.culture.date_fin))
    if req.culture.qte_recoltee is not None:
        newFieldValue.append(UpdateFieldValue(field="qte_recoltee", value=req.culture.qte_recoltee))
    return UpdateRequestDTO(
        table="culture",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="identifiant_culture", value=req.culture.identifiant_culture)
        ]
    )


def mapUpdateCultureRequestDto(request: UpdateCultureRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateCultureRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateCultureRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="culture",
            newFieldValue=[
                UpdateFieldValue(field="no_parcelle", value=request.culture.no_parcelle),
                UpdateFieldValue(field="code_production", value=request.culture.code_production),
                UpdateFieldValue(field="date_debut", value=request.culture.date_debut),
                UpdateFieldValue(field="date_fin", value=request.culture.date_fin),
                UpdateFieldValue(field="qte_recoltee", value=request.culture.qte_recoltee),
            ],
            identifiers=[
                UpdateFieldValue(field="identifiant_culture", value=request.culture.identifiant_culture)
            ]
        )


def mapInsertCultureRequestDto(request: PostCultureRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostCultureRequestDTO to a InsertRequestDTO\n
    :param request: PostCultureRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="culture",
            fieldValue=[
                FieldValue(field="no_parcelle", value=request.culture.no_parcelle),
                FieldValue(field="code_production", value=request.culture.code_production),
                FieldValue(field="date_debut", value=request.culture.date_debut),
                FieldValue(field="date_fin", value=request.culture.date_fin),
                FieldValue(field="qte_recoltee", value=request.culture.qte_recoltee),
            ]
        )


def mapDeleteCultureRequestDto(identifiant_culture: int) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param identifiant_culture:
    :return:
    """
    return DeleteItemRequestDTO(
            table="culture",
            identifiers=[
                IdValue(field="identifiant_culture", value=str(identifiant_culture))
            ]
        )