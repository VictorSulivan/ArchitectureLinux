from pydantic import BaseModel


########## PARCELLE ##########


### POST ###
class EpandreDTO(BaseModel):
    id_engrais: str
    no_parcelle: str
    date: str
    qte_epandue: str


class PostEpandreRequestDTO(BaseModel):
    epandre: EpandreDTO


class EpandreResponseDTO(BaseModel):
    message: str
    epandre: EpandreDTO


### PATCH ###
class PatchEpandreDTO(BaseModel):
    id_engrais: str = None
    no_parcelle: str = None
    date: str = None
    qte_epandue: str = None


class PatchEpandreRequestDTO(BaseModel):
    epandre: PatchEpandreDTO
    identifiers: PatchEpandreDTO


### PUT ###
class UpdateEpandreDTO(BaseModel):
    id_engrais: str
    no_parcelle: str
    date: str
    qte_epandue: str


class UpdateEpandreIdentifiersDTO(BaseModel):
    id_engrais: str
    no_parcelle: str
    date: str


class UpdateEpandreRequestDTO(BaseModel):
    epandre: UpdateEpandreDTO
    identifiers: UpdateEpandreIdentifiersDTO





