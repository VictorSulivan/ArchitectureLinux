from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.ParcelleDTO import ParcelleDTO, PostParcelleRequestDTO, ParcelleResponseDTO, PatchParcelleRequestDTO, \
    UpdateParcelleRequestDTO


def mapPatchParcelleRequestDto(req: PatchParcelleRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchParcelleRequestDTO to a UpdateRequestDTO\n
    :param req: PatchParcelleRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    if req.parcelle.surface is not None:
        newFieldValue.append(UpdateFieldValue(field="surface", value=req.parcelle.surface))
    if req.parcelle.nom_parcelle is not None:
        newFieldValue.append(UpdateFieldValue(field="nom_parcelle", value=req.parcelle.nom_parcelle))
    if req.parcelle.coordonnees is not None:
        newFieldValue.append(UpdateFieldValue(field="coordonnees", value=req.parcelle.coordonnees))
    return UpdateRequestDTO(
        table="parcelle",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="no_parcelle", value=req.parcelle.no_parcelle)
        ]
    )


def mapUpdateParcelleRequestDto(request: UpdateParcelleRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateParcelleRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateParcelleRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="parcelle",
            newFieldValue=[
                UpdateFieldValue(field="surface", value=request.parcelle.surface),
                UpdateFieldValue(field="nom_parcelle", value=request.parcelle.nom_parcelle),
                UpdateFieldValue(field="coordonnees", value=request.parcelle.coordonnees),
            ],
            identifiers=[
                UpdateFieldValue(field="no_parcelle", value=request.parcelle.no_parcelle)
            ]
        )


def mapInsertParcelleRequestDto(request: PostParcelleRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostParcelleRequestDTO to a InsertRequestDTO\n
    :param request: PostParcelleRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="parcelle",
            fieldValue=[
                FieldValue(field="surface", value=request.parcelle.surface),
                FieldValue(field="nom_parcelle", value=request.parcelle.nom_parcelle),
                FieldValue(field="coordonnees", value=request.parcelle.coordonnees)
            ]
        )


def mapDeleteParcelleRequestDto(no_parcelle: int) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param no_parcelle:
    :return:
    """
    return DeleteItemRequestDTO(
            table="parcelle",
            identifiers=[
                IdValue(field="no_parcelle", value=str(no_parcelle))
            ]
        )