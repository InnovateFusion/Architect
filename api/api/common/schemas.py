from typing import Optional
from pydantic import BaseModel

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
    future_proofing: list[str]
    cultural_religious: list[str]
    budget_range: str
    family_size: str
    security_safety: str
    outdoor_spaces: str
    vehicles_parking: str
    budget_allocation: str
    home_space: str
    atmosphere_ambiance: str
    design_inspirations: str
    smart_home_technology: str
    weather_concerns: str
    construction_phasing: str

class HomeUpdate(HomeBase):
    future_proofing: list[str]
    cultural_religious: list[str]
    budget_range: str
    family_size: str
    security_safety: str
    outdoor_spaces: str
    vehicles_parking: str
    budget_allocation: str
    home_space: str
    atmosphere_ambiance: str
    design_inspirations: str
    smart_home_technology: str
    weather_concerns: str
    construction_phasing: str


class BusinessCreate(HomeBase):
    building_purpose: str
    total_square_footage: str
    architectural_style: str
    sustainability_goals: list[str]
    number_of_floors: str
    zoning_constraints: str
    number_of_occupants: str
    specialized_spaces_required: str
    accessibility_requirements: str
    amenities: str
    parking_spaces: str
    interior_exterior_ambiance: str
    design_inspirations: list[str]
    technology_integration: str
    weather_site_challenges: str
    construction_phasing: str
    
        
class BusinessUpdate(HomeBase):
    building_purpose: str
    total_square_footage: str
    architectural_style: str
    sustainability_goals: list[str]
    number_of_floors: str
    zoning_constraints: str
    number_of_occupants: str
    specialized_spaces_required: str
    accessibility_requirements: str
    amenities: str
    parking_spaces: str
    interior_exterior_ambiance: str
    design_inspirations: list[str]
    technology_integration: str
    weather_site_challenges: str
    construction_phasing: str
    
class Home(HomeBase):
    id: str
    user_id: str
    data: dict
    
    class Config:
        arbitrary_types_allowed=True