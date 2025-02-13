from sqlalchemy import Column, Integer, String
from database import Base


class SocialNetworksORM(Base):
    __tablename__ = 'social_networks'

    id = Column(Integer, primary_key = True, index = True)
    url = Column(String(150), nullable = False)
    icon = Column(String(100), nullable = False)
