# This application consists of three parts: Flask, Graphene, and SQLAlchemy
# This file is the graphene support.

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType as sqlaot
import db

class Church(sqlaot):
    class Meta:
        model = db.Church

class Person(sqlaot):
    class Meta:
        model = db.Person


def pg_name(parent, info):
    person = parent.person.name
    role = ""
    if parent.role:
        role = f", {parent.role.name}"
    return person + role

class Group(sqlaot):
    class Meta:
        model = db.Group
    person_names = graphene.List(graphene.String)

    def resolve_person_names(parent, info):
        return [pg_name(pg, None) for pg in parent.membership]

class PersonGroup(sqlaot):
    class Meta:
        model = db.PersonGroup
    name = graphene.String()

    def resolve_name(parent, info):
        return pg_name(parent, info)

class Role(sqlaot):
    class Meta:
        model = db.Role

class Query(graphene.ObjectType):
    churches = graphene.List(Church)
    church = graphene.List(Church)

    def resolve_churches(self, info):
        query = Church.get_query(info)
        return query.all()

schema = graphene.Schema(query=Query)
