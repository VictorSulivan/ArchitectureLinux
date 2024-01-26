from pydantic import BaseModel


########## PARCELLE ##########


### POST ###
class ParcelleDTO(BaseModel):
    nom_parcelle: str
    surface: str
    coordonnees: str


class PostParcelleRequestDTO(BaseModel):
    parcelle: ParcelleDTO


class ParcelleResponseDTO(BaseModel):
    message: str
    culture: ParcelleDTO


### PATCH ###
class PatchParcelleDTO(BaseModel):
    no_parcelle: str
    surface: str = None
    nom_parcelle: str = None
    coordonnees: str = None


class PatchParcelleRequestDTO(BaseModel):
    parcelle: PatchParcelleDTO


### PUT ###
class UpdateParcelleDTO(BaseModel):
    no_parcelle: str
    surface: str
    nom_parcelle: str
    coordonnees: str


class UpdateParcelleRequestDTO(BaseModel):
    parcelle: UpdateParcelleDTO





