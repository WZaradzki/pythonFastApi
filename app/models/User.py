from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Index

from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

from models.Role import Role
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


RELATION_ROLE: str = 'Role'
Roles: str = 'roles'


class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True)
    name = Column(String(30))
    surname = Column(String(50))
    email = Column(String(50))
    role_id = Column(String(50), ForeignKey(Role.id), nullable=True)


Index('name_surname_index', User.name, User.surname)
Index('email_index', User.email)
user = relationship(RELATION_ROLE, back_populates=Roles)


class Model(BaseModel):
    id: str
    name: str
    surname: str
    email: str
    role_id: str | None
