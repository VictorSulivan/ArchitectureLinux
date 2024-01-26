from pydantic import BaseModel


########## Date ##########


### POST ###
class DateDTO(BaseModel):
    date: str


class PostDateRequestDTO(BaseModel):
    date: DateDTO


class DateResponseDTO(BaseModel):
    message: str
    date: DateDTO


### PATCH ###
class PatchDateDTO(BaseModel):
    date: str


class PatchDateRequestDTO(BaseModel):
    date: PatchDateDTO
    identifier: PatchDateDTO


### PUT ###
class UpdateDateDTO(BaseModel):
    date: str


class UpdateDateRequestDTO(BaseModel):
    date: UpdateDateDTO
    identifier: UpdateDateDTO




