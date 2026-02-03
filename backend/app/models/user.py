import os
import uuid
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Boolean,
    Float,
    Text,
    TIMESTAMP,
    JSON,
    ForeignKey,
    text
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# ======================================================
# LOAD ENV
# ======================================================
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ======================================================
# CREATE DATABASE IF NOT EXISTS (SAFE)
# ======================================================
try:
    con = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute(
        "SELECT 1 FROM pg_database WHERE datname = %s",
        (DB_NAME,)
    )
    exists = cur.fetchone()
    if not exists:
        print(f"Creating database {DB_NAME}...")
        cur.execute(f'CREATE DATABASE "{DB_NAME}"')
    else:
        print(f"Database {DB_NAME} already exists.")
    cur.close()
    con.close()
except Exception as e:
    print("Database check failed:", e)

# ======================================================
# SQLALCHEMY BASE
# ======================================================
Base = declarative_base()

# ======================================================
# TABLE DEFINITIONS
# ======================================================

class Admin(Base):
    __tablename__ = "admin"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100))
    mobile_number = Column(String(20))
    role = Column(String(20))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    last_login = Column(TIMESTAMP)


class Call(Base):
    __tablename__ = "calls"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    call_id = Column(String(100), unique=True)
    scammer_phone = Column(String(20))
    target_phone = Column(String(20))
    call_source = Column(String(50))
    audio_file_path = Column(Text)
    transcript = Column(Text)
    risk_score = Column(Float)
    is_scam = Column(Boolean)
    ai_handoff = Column(Boolean)
    call_status = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now())


class CallExtractedData(Base):
    __tablename__ = "call_extracted_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    call_id = Column(UUID(as_uuid=True), ForeignKey("calls.id", ondelete="CASCADE"))
    upi_ids = Column(JSON)
    bank_accounts = Column(JSON)
    ifsc_codes = Column(JSON)
    phishing_links = Column(JSON)
    keywords_detected = Column(JSON)
    confidence_score = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())


class HoneypotConversation(Base):
    __tablename__ = "honeypot_conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    call_id = Column(UUID(as_uuid=True), ForeignKey("calls.id", ondelete="CASCADE"))
    speaker = Column(String(20))
    message = Column(Text)
    timestamp = Column(TIMESTAMP, server_default=func.now())

# ======================================================
# CREATE TABLES
# ======================================================
engine = create_engine(DATABASE_URL, echo=True)

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ PostgreSQL tables created successfully!")
