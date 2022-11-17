from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Index

from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
# metadata = sqlalchemy.MetaData()

# notes = sqlalchemy.Table(
#     "notes",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("text", sqlalchemy.String),
#     sqlalchemy.Column("completed", sqlalchemy.Boolean),
# )
# class User(BaseModel):
#     name: str
#     surname: str | None = None
#     email: str

Base = declarative_base()

User = 'user'

RELATION_USERS = 'Users'


class Role(Base):
    __tablename__ = "roles"

    id = Column(String(50), primary_key=True)
    name = Column(String(30))


Index('name_index', Role.name)
users = relationship(
    RELATION_USERS, back_populates=User, cascade="all, delete-orphan"
)
