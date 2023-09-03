from typing import Optional, List
from pydantic import BaseModel


class Chat(BaseModel):
    chat: str
    class Config:
        arbitrary_types_allowed=True

class UserBase(BaseModel):
    email: str
    firstname: str
    lastname: str
    type: str
    profile_image: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed=True
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: str
    
class UserUpdate(UserBase):
    password: Optional[str] = None
    

class HomeBase(BaseModel):
    title: str
    type: str
    
    class Config:
        arbitrary_types_allowed=True

class HomeCreate(HomeBase):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str
    question6: str
    question7: str
    question8: str
    question9: str
    question10: str
    question11: str
    question12: str
    question13: str
    question14: str
    

class HomeUpdate(HomeBase):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str
    question6: str
    question7: str
    question8: str
    question9: str
    question10: str
    question11: str
    question12: str
    question13: str
    question14: str


class BusinessCreate(HomeBase):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str
    question6: str
    question7: str
    question8: str
    question9: str
    question10: str
    question11: str
    question12: str
    question13: str
    question14: str
    question15: str
    
        
class BusinessUpdate(HomeBase):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str
    question6: str
    question7: str
    question8: str
    question9: str
    question10: str
    question11: str
    question12: str
    question13: str
    question14: str
    question15: str
    
class Home(HomeBase):
    id: str
    user_id: str
    data: dict
    
    class Config:
        arbitrary_types_allowed=True