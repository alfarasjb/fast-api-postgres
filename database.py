import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# This is not working. Auth error (Wrong pass ???)
DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/fastapi_database"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()


# Create a session
session = SessionLocal()

# Example: Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")

# Don't forget to close the session when done
session.close()
