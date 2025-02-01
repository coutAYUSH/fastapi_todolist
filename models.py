from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel,Field

class Lists(Base):
    __tablename__ = "Tasks"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False,unique=True, index=True)
   


