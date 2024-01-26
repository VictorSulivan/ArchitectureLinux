from pydantic import BaseModel


########## CULTURE ##########


### POST ###
class CultureDTO(BaseModel):
    no_parcelle: str
    code_production: str
    date_debut: str
    date_fin: str
    qte_recoltee: str


class PostCultureRequestDTO(BaseModel):
    culture: CultureDTO


class CultureResponseDTO(BaseModel):
    message: str
    culture: CultureDTO


### PATCH ###
class PatchCultureDTO(BaseModel):
    identifiant_culture: str
    no_parcelle: str = None
    code_production: str = None
    date_debut: str = None
    date_fin: str = None
    qte_recoltee: str = None


class PatchCultureRequestDTO(BaseModel):
    culture: PatchCultureDTO


### PUT ###
class UpdateCultureDTO(BaseModel):
    identifiant_culture: str
    no_parcelle: str
    code_production: str
    date_debut: str
    date_fin: str
    qte_recoltee: str


class UpdateCultureRequestDTO(BaseModel):
    culture: UpdateCultureDTO





