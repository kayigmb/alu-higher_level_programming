#!/usr/bin/python3
"""
commenting done
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session1 = Session()
    Base.metadata.create_all(engine)

    state = State(name="Louisiana")
    session1.add(state)
    session1.commit()
    print("{}".format(state.id))
    session1.close()
