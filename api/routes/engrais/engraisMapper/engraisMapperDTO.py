from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.EngraisDTO import EngraisDTO, PostEngraisRequestDTO, EngraisResponseDTO, PatchEngraisRequestDTO, \
    UpdateEngraisRequestDTO


def mapPatchEngraisRequestDto(req: PatchEngraisRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchEngraisRequestDTO to a UpdateRequestDTO\n
    :param req: PatchEngraisRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    if req.engrais.un is not None:
        newFieldValue.append(UpdateFieldValue(field="un", value=req.engrais.un))
    if req.engrais.nom_engrais is not None:
        newFieldValue.append(UpdateFieldValue(field="nom_engrais", value=req.engrais.nom_engrais))
    return UpdateRequestDTO(
        table="engrais",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="id_engrais", value=req.engrais.id_engrais)
        ]
    )


def mapUpdateEngraisRequestDto(request: UpdateEngraisRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateEngraisRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateEngraisRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="engrais",
            newFieldValue=[
                UpdateFieldValue(field="un", value=request.engrais.un),
                UpdateFieldValue(field="nom_engrais", value=request.engrais.nom_engrais),
            ],
            identifiers=[
                UpdateFieldValue(field="id_engrais", value=request.engrais.id_engrais)
            ]
        )


def mapInsertEngraisRequestDto(request: PostEngraisRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostEngraisRequestDTO to a InsertRequestDTO\n
    :param request: PostEngraisRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="engrais",
            fieldValue=[
                FieldValue(field="un", value=request.engrais.un),
                FieldValue(field="nom_engrais", value=request.engrais.nom_engrais),
            ]
        )


def mapDeleteEngraisRequestDto(id_engrais: int) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param id:
    :return:
    """
    return DeleteItemRequestDTO(
            table="engrais",
            identifiers=[
                IdValue(field="id_engrais", value=str(id_engrais))
            ]
        )