from routes.dtoModel.DatasourceDTO import FieldValue, IdValue, OrderDTO, SelectRequestDTO, DeleteItemRequestDTO, \
    UpdateFieldValue, UpdateRequestDTO, InsertRequestDTO
from routes.dtoModel.ElementChimiqueDTO import ElementChimiqueDTO, PostElementChimiqueRequestDTO, PatchElementChimiqueRequestDTO, \
    UpdateElementChimiqueRequestDTO


def mapPatchElementChimiqueRequestDto(req: PatchElementChimiqueRequestDTO) -> UpdateRequestDTO:
    """
    description: map a PatchElementChimiqueRequestDTO to a UpdateRequestDTO\n
    :param req: PatchElementChimiqueRequestDTO
    :return: UpdateRequestDTO
    """
    newFieldValue = []
    if req.elementChimique.un is not None:
        newFieldValue.append(UpdateFieldValue(field="un", value=req.elementChimique.un))
    if req.elementChimique.libelle_element is not None:
        newFieldValue.append(UpdateFieldValue(field="libelle_element", value=req.elementChimique.libelle_element))
    return UpdateRequestDTO(
        table="elements_chimiques",
        newFieldValue=newFieldValue,
        identifiers=[
            UpdateFieldValue(field="code_element", value=req.elementChimique.code_element)
        ]
    )


def mapUpdateElementChimiqueRequestDto(request: UpdateElementChimiqueRequestDTO) -> UpdateRequestDTO:
    """
    description: map a UpdateElementChimiqueRequestDTO to a UpdateRequestDTO\n
    :param request: UpdateElementChimiqueRequestDTO
    :return: UpdateRequestDTO
    """
    return UpdateRequestDTO(
            table="elements_chimiques",
            newFieldValue=[
                UpdateFieldValue(field="un", value=request.elementChimique.un),
                UpdateFieldValue(field="libelle_element", value=request.elementChimique.libelle_element),
            ],
            identifiers=[
                UpdateFieldValue(field="code_element", value=request.elementChimique.code_element)
            ]
        )


def mapInsertElementChimiqueRequestDto(request: PostElementChimiqueRequestDTO) -> InsertRequestDTO:
    """
    description: map a PostElementChimiqueRequestDTO to a InsertRequestDTO\n
    :param request: PostElementChimiqueRequestDTO
    :return: InsertRequestDTO
    """
    return InsertRequestDTO(
            table="elements_chimiques",
            fieldValue=[
                FieldValue(field="code_element", value=request.elementChimique.code_element),
                FieldValue(field="un", value=request.elementChimique.un),
                FieldValue(field="libelle_element", value=request.elementChimique.libelle_element)
            ]
        )


def mapDeleteElementChimiqueRequestDto(code_element: str) -> DeleteItemRequestDTO:
    """
    description: map a id to a DeleteItemRequestDTO\n
    :param code_element:
    :return:
    """
    return DeleteItemRequestDTO(
            table="elements_chimiques",
            identifiers=[
                IdValue(field="code_element", value=str(code_element))
            ]
        )