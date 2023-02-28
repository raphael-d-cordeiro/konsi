from core.configs import settings
from sqlalchemy import Column, Integer, Float, String, Date


class BotModel(settings.DBBaseModel):
    __tablename__ = 'bots'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    cpf: str = Column(String(15), unique=True, index=True, nullable=False)
    nome: str = Column(String(256), unique=True, index=True, nullable=False)
    email: str = Column(String(256), unique=True, index=True, nullable=False)
    data_nascimento: Date = Column(Date)
    sexo: str = Column(String(1))
    renda_mensal: float = Column(Float, default=0.0)
