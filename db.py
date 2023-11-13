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

person_group = Table(
        "person_group",
        Base.metadata,
        Column("person_id", ForeignKey("person.id"), primary_key=True),
        Column("group_id", ForeignKey("group_.id"), primary_key=True),
        )

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    groups = relationship("Group", secondary=person_group, back_populates="persons")

class Group(Base):
    __tablename__ = "group_"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    church_id = Column(Integer, ForeignKey("church.id"), nullable=False)
    church = relationship("Church", back_populates="groups")

    persons = relationship("Person", secondary=person_group, back_populates="groups")
