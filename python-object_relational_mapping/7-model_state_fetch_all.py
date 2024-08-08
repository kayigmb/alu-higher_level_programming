#!/usr/bin/python3
"""
commenitng is done
"""


import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session1 = Session()
    states = session1.query(State).order_by(State.id).all()
    for i in states:
        print("{}: {}".format(i.id, i.name))
