from sqlalchemy import Column, Integer, String
from database import Base


class ProjectsORM(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key = True, index = True)
    git_id = Column(Integer, nullable = False)
    title = Column(String(255), nullable = True)
    description = Column(String(255), nullable = True)
    image_url = Column(String(150), nullable = True)
    live_url = Column(String(150), nullable = True)
    repo_url = Column(String(150), nullable = True)
