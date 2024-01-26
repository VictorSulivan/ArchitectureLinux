from pydantic import BaseModel


########## ELEMENT CHIMIQUE ##########


### POST ###
class ElementChimiqueDTO(BaseModel):
    code_element: str
    un: str
    libelle_element: str


class PostElementChimiqueRequestDTO(BaseModel):
    elementChimique: ElementChimiqueDTO


### PATCH ###
class PatchElementChimiqueDTO(BaseModel):
    code_element: str
    un: str = None
    libelle_element: str = None


class PatchElementChimiqueRequestDTO(BaseModel):
    elementChimique: PatchElementChimiqueDTO


### PUT ###
class UpdateElementChimiqueDTO(BaseModel):
    code_element: str
    un: str
    libelle_element: str


class UpdateElementChimiqueRequestDTO(BaseModel):
    elementChimique: UpdateElementChimiqueDTO





