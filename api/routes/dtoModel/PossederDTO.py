from pydantic import BaseModel


########## POSSEDER ##########


### POST ###
class PossederDTO(BaseModel):
    id_engrais: str
    code_element: str
    valeur: str


class PostPossederRequestDTO(BaseModel):
    posseder: PossederDTO


class PossederResponseDTO(BaseModel):
    message: str
    posseder: PossederDTO


### PATCH ###
class PatchPossederDTO(BaseModel):
    id_engrais: str = None
    code_element: str = None
    valeur: str = None


class PatchPossederRequestDTO(BaseModel):
    posseder: PatchPossederDTO
    identifiers: PatchPossederDTO


### PUT ###
class UpdatePossederDTO(BaseModel):
    id_engrais: str
    code_element: str
    valeur: str


class UpdatePossederIdentifiersDTO(BaseModel):
    id_engrais: str
    code_element: str


class UpdatePossederRequestDTO(BaseModel):
    posseder: UpdatePossederDTO
    identifiers: UpdatePossederIdentifiersDTO





