#!/usr/bin/python3
"""
commenting
"""


import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    db_engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=db_engine)
    Base.metadata.create_all(db_engine)
    session = Session()
    states = session.query(State).filter(State.name.contains("a")).all()
    for i in states:
        print(f"{i.id}: {i.name}")
    session.close()
