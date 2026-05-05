#test for config
import pytest
from sqlalchemy import create_url, create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base

#use sqlite database for speed 
TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def db_session():
    #setup the engine and session
    engine = create_engine(TEST_DATABASE_URL,
connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False,
autoflush=False, bind=engine)
    
    #create table in test database 
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

    #drop table after test is done
    Base.metadata.drop_all(bind=engine)