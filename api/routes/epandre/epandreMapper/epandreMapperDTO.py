from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.EpandreDTO import EpandreDTO, PostEpandreRequestDTO, EpandreResponseDTO, PatchEpandreRequestDTO, \
    UpdateEpandreRequestDTO


def mapPatchEpandreRequestDto(req: PatchEpandreRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchEpandreRequestDTO to a UpdateRequestDTO\n
    :param req: PatchEpandreRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    if req.epandre.id_engrais is not None:
        newFieldValue.append(UpdateFieldValue(field="id_engrais", value=req.epandre.id_engrais))
    if req.epandre.no_parcelle is not None:
        newFieldValue.append(UpdateFieldValue(field="no_parcelle", value=req.epandre.no_parcelle))
    if req.epandre.date is not None:
        newFieldValue.append(UpdateFieldValue(field="date", value=req.epandre.date))
    if req.epandre.qte_epandue is not None:
        newFieldValue.append(UpdateFieldValue(field="qte_epandue", value=req.epandre.qte_epandue))
    return UpdateRequestDTO(
        table="epandre",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="id_engrais", value=req.identifiers.id_engrais),
            UpdateFieldValue(field="no_parcelle", value=req.identifiers.no_parcelle),
            UpdateFieldValue(field="date", value=req.identifiers.date)
        ]
    )


def mapUpdateEpandreRequestDto(request: UpdateEpandreRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateEpandreRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateEpandreRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="epandre",
            newFieldValue=[
                UpdateFieldValue(field="id_engrais", value=request.epandre.id_engrais),
                UpdateFieldValue(field="no_parcelle", value=request.epandre.no_parcelle),
                UpdateFieldValue(field="date", value=request.epandre.date),
                UpdateFieldValue(field="qte_epandue", value=request.epandre.qte_epandue),
            ],
            identifiers=[
                UpdateFieldValue(field="id_engrais", value=request.identifiers.id_engrais),
                UpdateFieldValue(field="no_parcelle", value=request.identifiers.no_parcelle),
                UpdateFieldValue(field="date", value=request.identifiers.date)
            ]
        )


def mapInsertEpandreRequestDto(request: PostEpandreRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostEpandreRequestDTO to a InsertRequestDTO\n
    :param request: PostEpandreRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="epandre",
            fieldValue=[
                FieldValue(field="id_engrais", value=request.epandre.id_engrais),
                FieldValue(field="no_parcelle", value=request.epandre.no_parcelle),
                FieldValue(field="date", value=request.epandre.date),
                FieldValue(field="qte_epandue", value=request.epandre.qte_epandue)
            ]
        )


def mapDeleteEpandreRequestDto(id_engrais: int, no_parcelle: int, date: str) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param id:
    :return:
    """
    return DeleteItemRequestDTO(
            table="epandre",
            identifiers=[
                IdValue(field="id_engrais", value=str(id_engrais)),
                IdValue(field="no_parcelle", value=str(no_parcelle)),
                IdValue(field="date", value=date)
            ]
        )