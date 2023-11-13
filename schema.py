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

class Group(sqlaot):
    class Meta:
        model = db.Group

class Query(graphene.ObjectType):
    churches = graphene.List(Church)
    church = graphene.List(Church, 

    def resolve_churches(self, info):
        query = Church.get_query(info)
        return query.all()

schema = graphene.Schema(query=Query)
