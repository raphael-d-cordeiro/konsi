from typing import Optional, Any

from pydantic import BaseModel as SCBaseModel
from pydantic import Json, root_validator
from datetime import date


class CrawlerSchemaPost(SCBaseModel):
    document: str
    username: str
    password: str

    @root_validator
    def check_cpf_cnpj(cls, values):
        document = values["document"]
        # TODO: create a customized exception
        try:
            assert len(document) == 14
            assert document[3] == '.'
            assert document[7] == '.'
            assert document[11] == '-'
        except AssertionError:
            raise Exception('CPF must have 14 digits. Ex: 074.687.335-20')

        return values

    class Config:
        schema_extra = {
            "example": {
                "document": "074.687.335-20",
                "username": "teste",
                "password": "teste",
            }
        }


class CrawlerSchemaResp(SCBaseModel):
    id: Optional[int]
    task_id: str
    document: str
    crawler_data: Json[Any]
    created_at: date

    class Config:
        orm_mode = True
