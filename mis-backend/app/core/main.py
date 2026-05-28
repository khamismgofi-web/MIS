from app.core.database import get_engine,Base
import models
print("Connecting to Neon and creating tables")
Base.metadata.create_all(bind=get_engine)
print("Tables created successfully")