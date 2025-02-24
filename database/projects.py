from sqlalchemy import Column, Integer, String
from database import Base


class ProjectsORM(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(255), nullable = False)
    description = Column(String(255), nullable = False)
    image_url = Column(String(150), nullable = True)
    live_url = Column(String(150), nullable = False)
    repo_url = Column(String(150), nullable = False)
