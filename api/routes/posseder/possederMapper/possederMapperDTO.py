from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.PossederDTO import PossederDTO, PostPossederRequestDTO, PossederResponseDTO, PatchPossederRequestDTO, \
    UpdatePossederRequestDTO


def mapPatchPossederRequestDto(req: PatchPossederRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchPossederRequestDTO to a UpdateRequestDTO\n
    :param req: PatchPossederRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    if req.posseder.id_engrais is not None:
        newFieldValue.append(UpdateFieldValue(field="id_engrais", value=req.posseder.id_engrais))
    if req.posseder.code_element is not None:
        newFieldValue.append(UpdateFieldValue(field="code_element", value=req.posseder.code_element))
    if req.posseder.valeur is not None:
        newFieldValue.append(UpdateFieldValue(field="valeur", value=req.posseder.valeur))
    return UpdateRequestDTO(
        table="posseder",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="id_engrais", value=req.identifiers.id_engrais),
            UpdateFieldValue(field="code_element", value=req.identifiers.code_element)
        ]
    )


def mapUpdatePossederRequestDto(request: UpdatePossederRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdatePossederRequestDTO to a UpdateRequestDTO\n
    :param request: UpdatePossederRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="posseder",
            newFieldValue=[
                UpdateFieldValue(field="id_engrais", value=request.posseder.id_engrais),
                UpdateFieldValue(field="code_element", value=request.posseder.code_element),
                UpdateFieldValue(field="valeur", value=request.posseder.valeur)
            ],
            identifiers=[
                UpdateFieldValue(field="id_engrais", value=request.identifiers.id_engrais),
                UpdateFieldValue(field="code_element", value=request.identifiers.code_element)
            ]
        )


def mapInsertPossederRequestDto(request: PostPossederRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostPossederRequestDTO to a InsertRequestDTO\n
    :param request: PostPossederRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="posseder",
            fieldValue=[
                FieldValue(field="id_engrais", value=request.posseder.id_engrais),
                FieldValue(field="code_element", value=request.posseder.code_element),
                FieldValue(field="valeur", value=request.posseder.valeur)
            ]
        )


def mapDeletePossederRequestDto(id_engrais: int, code_element: str) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param id_engrais:
    :param code_element:
    :return:
    """
    return DeleteItemRequestDTO(
            table="posseder",
            identifiers=[
                IdValue(field="id_engrais", value=str(id_engrais)),
                IdValue(field="code_element", value=str(code_element))
            ]
        )