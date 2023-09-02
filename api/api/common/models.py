from sqlalchemy import Column, String, ForeignKey,JSON, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True)
    email = Column(String(128), unique=True, index=True, nullable=True)
    firstname = Column(String(60), nullable=True)
    lastname = Column(String(60), nullable=True)
    user_type = Column(Enum("architect", "client"), nullable=False)
    password = Column(String(128))
    profile_image = Column(String(128))
    homes = relationship("Home", back_populates="user")
    
    def toJSON(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "user_type": self.user_type,
            "profile_image": self.profile_image
        }

    def __repr__(self):
        return f"<User(id={self.id}), firstname={self.firstname}>"

class Home(Base):
    __tablename__ = "homes"
    id = Column(String(36), primary_key=True, index=True)
    title = Column(String(128), nullable=False)
    home_type = Column(Enum("home", "business"), nullable=False)
    user_id = Column(String(36), ForeignKey("users.id")) 
    data = Column(JSON, nullable=True)
    context = Column(LONGTEXT, nullable=True)
    user = relationship("User", back_populates="homes")

    def toJSON(self):
        return {
            "id": self.id,
            "title": self.title,
            "home_type": self.home_type,
            "user_id": self.user_id,
            "data": self.data,
        }

    def __repr__(self):
        return f"<Home(id={self.id}), title={self.title}>"
    
