from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from db.base import Base

class Data(Base):
    __tablename__ = "h_data"
    
    id = Column(Integer, primary_key=True)
    file_data = Column(String(16000), nullable=False)