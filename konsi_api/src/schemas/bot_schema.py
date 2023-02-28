from typing import Optional

from pydantic import BaseModel as SCBaseModel
from pydantic import EmailStr
from datetime import date


class BotSchema(SCBaseModel):
    id: Optional[int]
    cpf: str
    nome: str
    email: EmailStr
    data_nascimento: date
    sexo: str
    renda_mensal: float

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "cpf": "45645645600",
                "nome": "José da Silva",
                "email": "jose@cliente.com",
                "data_nascimento": "2010-01-01",
                "sexo": "M",
                "renda_mensal": 2899.5
            }
        }
