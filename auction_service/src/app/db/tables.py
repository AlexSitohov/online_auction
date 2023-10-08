import uuid as _uuid
from sqlalchemy import (
    BOOLEAN,
    FLOAT,
    TEXT,
    Column,
    text,
    String,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimestampMixin(Base):
    __abstract__ = True
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted = Column(BOOLEAN, nullable=False, server_default="false", default=False)


class User(TimestampMixin):
    __tablename__ = "user"
    id = Column(
        UUID(as_uuid=False),
        primary_key=True,
        unique=True,
        nullable=False,
        default=_uuid.uuid4,
    )
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String, nullable=False)
    email = Column(String(30), nullable=False, unique=True)


class Lot(TimestampMixin):
    __tablename__ = "lot"
    id = Column(
        UUID(as_uuid=False),
        primary_key=True,
        unique=True,
        nullable=False,
        default=_uuid.uuid4,
    )
    description = Column(TEXT, nullable=False)
    starting_price = Column(FLOAT, nullable=False)
    end_time = Column(TIMESTAMP(timezone=True), nullable=False)


class Bid(TimestampMixin):
    __tablename__ = "bid"
    id = Column(
        UUID(as_uuid=False),
        primary_key=True,
        unique=True,
        nullable=False,
        default=_uuid.uuid4,
    )
    amount = Column(FLOAT, nullable=False)
    user_id = Column(ForeignKey("user.id"), primary_key=True, nullable=False)
    lot_id = Column(ForeignKey("lot.id"), primary_key=True, nullable=False)
