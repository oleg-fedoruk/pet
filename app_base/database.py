from sqlmodel import create_engine

eng = 'db.sqlite3'
sqlite_url = f'sqlite:///{eng}'
engine = create_engine(sqlite_url, echo=True)
