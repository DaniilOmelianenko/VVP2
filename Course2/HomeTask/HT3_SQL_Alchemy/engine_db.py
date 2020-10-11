from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///db.sqlite3", echo=True)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
