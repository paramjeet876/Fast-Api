from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(100), nullable=False)
    mobile_number = Column(String(15), unique=True, nullable=False)
    preferred_time = Column(String(50), nullable=False)
    procedure = Column(String(255), nullable=False)
    