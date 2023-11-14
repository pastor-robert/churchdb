# This application consists of three parts: Flask, Graphene, and SQLAlchemy
# This file is the SQLAlchemy support.

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///church.db')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()

class Church(Base):
    __tablename__ = "church"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    groups = relationship(
            "Group", back_populates="church", cascade="all, delete-orphan"
            )

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Group(Base):
    __tablename__ = "group_"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    church_id = Column(Integer, ForeignKey("church.id"), nullable=False)
    church = relationship("Church", back_populates="groups")

    persons = relationship("PersonGroup")


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class PersonGroup(Base):
    __tablename__ = "person_group"

    group_id = Column(ForeignKey("group_.id"), primary_key=True)
    person_id = Column(ForeignKey("person.id"), primary_key=True)
    person = relationship("Person")

    role_id = Column(ForeignKey("role.id"))
    role = relationship("Role")


