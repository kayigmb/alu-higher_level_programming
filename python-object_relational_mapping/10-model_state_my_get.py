#!/usr/bin/python3
"""
commenting
"""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session1 = Session()
    state = session1.query(State).filter_by(name=argv[4]).first()
    if not state:
        print("Not found")
    else:
        print("{:d}".format(state.id))
    session1.close()
