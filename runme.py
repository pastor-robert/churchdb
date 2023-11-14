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

    pastor = db.Role(name="Pastor")
    chair = db.Role(name="Chair")

    mtv = db.Church(name="Mt Vernon UMC", groups=[congo, council, choir])

    for p, g, r in (
            (rob, congo, pastor),
            (rr, congo, None),
            (bob, congo, None),
            (rob, choir, None),
            (rr, choir, None),
            (rob, council, pastor),
            (bob, council, chair),
            ):
        pg = db.PersonGroup()
        pg.person = p
        pg.role = r
        g.persons.append(pg)

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
