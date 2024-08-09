import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# Update the DATABASE_URL with the correct user, password, and database name
DATABASE_URL = "postgresql://myuser:password@localhost:5621/fastapi_database"


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
