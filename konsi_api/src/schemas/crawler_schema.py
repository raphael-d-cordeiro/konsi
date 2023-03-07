from typing import Optional, Any

from pydantic import BaseModel as SCBaseModel
from pydantic import root_validator


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
