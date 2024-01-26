from pydantic import BaseModel


########## DATA SOURCE ##########


### INSERT ###
class UpdateFieldValue(BaseModel):
    field: str
    value: str


class UpdateRequestDTO(BaseModel):
    table: str
    newFieldValue: list[UpdateFieldValue]
    identifiers: list[UpdateFieldValue]


### SELECT ###
class OrderDTO(BaseModel):
    field: str
    type: str


class ConditionDTO(BaseModel):
    field: str
    value: str


class SelectRequestDTO(BaseModel):
    table: str
    selectedFields: list[str]
    conditions: list[ConditionDTO] = None
    order: OrderDTO
    id: str


### DELETE ###
class IdValue(BaseModel):
    field: str
    value: str


class DeleteItemRequestDTO(BaseModel):
    table: str
    identifiers: list[IdValue]


### INSERT ###
class FieldValue(BaseModel):
    field: str
    value: str


class InsertRequestDTO(BaseModel):
    table: str
    fieldValue: list[FieldValue]
