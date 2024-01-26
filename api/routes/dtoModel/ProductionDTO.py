from pydantic import BaseModel


########## PRODUCTION ##########


### POST ###
class ProductionDTO(BaseModel):
    un : str
    nom_production : str


class PostProductionRequestDTO(BaseModel):
    production: ProductionDTO


### PATCH ###
class PatchProductionDTO(BaseModel):
    code_production: str
    un: str = None
    nom_production: str = None


class PatchProductionRequestDTO(BaseModel):
    production: PatchProductionDTO


### PUT ###
class UpdateProductionDTO(BaseModel):
    code_production: str
    un: str
    nom_production: str


class UpdateProductionRequestDTO(BaseModel):
    production: UpdateProductionDTO




