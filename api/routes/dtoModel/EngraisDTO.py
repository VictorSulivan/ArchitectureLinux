from pydantic import BaseModel


########## ENGRAIS ##########


### POST ###
class EngraisDTO(BaseModel):
    un: str
    nom_engrais: str


class PostEngraisRequestDTO(BaseModel):
    engrais: EngraisDTO


class EngraisResponseDTO(BaseModel):
    message: str
    engrais: EngraisDTO


### PATCH ###
class PatchEngraisDTO(BaseModel):
    id_engrais: str
    un: str = None
    nom_engrais: str = None


class PatchEngraisRequestDTO(BaseModel):
    engrais: PatchEngraisDTO


### PUT ###
class UpdateEngraisDTO(BaseModel):
    id_engrais: str
    un: str
    nom_engrais: str


class UpdateEngraisRequestDTO(BaseModel):
    engrais: UpdateEngraisDTO
