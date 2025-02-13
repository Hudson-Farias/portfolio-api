from sqlalchemy import Column, Integer, String
from database import Base


class SkillsCategoriesORM(Base):
    __tablename__ = 'skills_categories'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(255), nullable = False)
