from app.db.session import engine
from app.db import models

def init_db():
    models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("✅ Database tables created")