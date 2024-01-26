from pydantic import BaseModel


########## Unite ##########


### POST ###
class UniteDTO(BaseModel):
    un: str


class PostUniteRequestDTO(BaseModel):
    unite: UniteDTO


class UniteResponseDTO(BaseModel):
    message: str
    unite: UniteDTO


### PATCH ###
class PatchUniteDTO(BaseModel):
    un: str


class PatchUniteRequestDTO(BaseModel):
    unite: PatchUniteDTO
    identifier: PatchUniteDTO


### PUT ###
class UpdateUniteDTO(BaseModel):
    un: str


class UpdateUniteRequestDTO(BaseModel):
    unite: UpdateUniteDTO
    identifier: UpdateUniteDTO




