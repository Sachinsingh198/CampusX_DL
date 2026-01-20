from pydantic import BaseModel, EmailStr,AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length = 50, title = 'Name of the patient',description= 'Give the name of the patient in maximun 50 words', examples = ['Nitish', 'Sachin'] )]
    email: EmailStr
    linkedin_url: AnyUrl
    age : int = Field(gt=0)
    weight: Annotated[float, Field(gt = 0, strict = True, description = 'Weight of the patient in kg', example = 75.5)]
    married : Annotated[bool, Field(default = None, description = 'Is the Patient married or not')]
    allergies : Optional[List[str]] = Field(max_lenght = 5) # Optional is used in case whent the data is optional not mandatory
    contact_details: Dict[str, str] 
    

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('Inserted')


def update_patient_data(patient: Patient):
    
    print(patient.name)

    print((patient.age))
    print('Update')


patient_info = {'name':'nitish','email': 'abc@gmail.com','linkedin_url':'http://linkedin.com/1234', 'age': 7, 'weight' : 75.2, 'married': True, 'allergies': ['pollen', 'dust', 'rhinitis'], 'contact_details':{ 'phone':'8191980879'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)