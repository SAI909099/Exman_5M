from datetime import datetime, tzinfo
from enum import Enum

from sqlalchemy import BigInteger, VARCHAR, Enum as alEnum, TEXT, DECIMAL, SMALLINT, ForeignKey, func, FunctionElement
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


class CreatedModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at = Column(DateTime(), default=func.current_timestamp())
    updated_at = Column(DateTime(), default=func.current_timestamp(), onupdate=func.current_timestamp())


class User(CreatedModel):
    class LangEnum(Enum):
        EN = "en"
        UZ = "uz"

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255))
    lang: Mapped[str] = mapped_column(alEnum(LangEnum, values_callable=lambda i: [field.value for field in i]),
                                      default=LangEnum.EN)
    phone_number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return self.full_name

