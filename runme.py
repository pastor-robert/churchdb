import db
import schema
import pprint
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///church.db", echo=True, future=True)
db.Base.metadata.create_all(engine)


with Session(engine) as session:
    rob = db.Person(name="Rob Adams")
    rr = db.Person(name="RR");
    bob = db.Person(name="Bob");

    congo = db.Group(name="congregation", )
    council = db.Group(name="council")
    choir = db.Group(name="choir")

    mtv = db.Church(name="Mt Vernon UMC", groups=[congo, council, choir])

    rob.groups.extend([congo, council, choir])
    rr.groups.extend([congo, choir])
    bob.groups.extend([congo, council])

    print(bob.groups)
    print(council.persons)

    session.add_all([mtv])
    session.commit()

query = '''
    query {
        churches {
            name
        }
    }
'''

with Session(engine) as session:
    result = schema.schema.execute(query, context_value={'session':session})
    pprint.pprint(result)
