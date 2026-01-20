from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional , Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode = 'after')
    @classmethod
    def age_checker(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should between 0 and 100')
    # Example: If you want to run a validator before type validation, use mode="before"
    # @field_validator('age', mode='before')  # 'mode="before"' runs before type validation.
    # @classmethod
    # def age_checker_before(cls, value):
    #     # You can add logic here to preprocess or clean up the raw input before parsing.
    #     return value

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.email)
    print('Updated Successfully')

patient_info = {'name':'nitish','email': 'abc@hdfc.com', 'age': '30', 'weight' : 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{ 'phone':'8191980879'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)