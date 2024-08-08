#!/usr/bin/python3
"""commenting this document"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = (
        session.query(State, City)
        .filter(State.id == City.state_id)
        .order_by(City.id)
        .all()
    )
    for i in states:
        print(
            "{}: ({}) {}".format(
                i[0].__dict__["name"],
                i[1].__dict__["id"],
                i[1].__dict__["name"],
            )
        )
    session.close()
