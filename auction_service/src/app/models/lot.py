from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class LotModel:
    class Base(BaseModel):
        description: str
        starting_price: float
        end_time: datetime

        class Config:
            from_attributes = True

    class GET(Base):
        id: UUID

    class POST(Base):
        ...

    class PUT(Base):
        ...
