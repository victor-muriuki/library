# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from .models import Base

# DATABASE_URL = "sqlite:///library.db"

# # Create a database engine
# engine = create_engine(DATABASE_URL)

# # Create the tables
# Base.metadata.create_all(bind=engine)

# # Create a session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def init_db():
#     # This function is used to initialize the database, e.g., when running migrations
#     Base.metadata.create_all(bind=engine)
#     print("Database initialized.")
