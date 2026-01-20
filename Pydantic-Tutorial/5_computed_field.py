from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional , Annotated

class Patient(BaseModel):
    name : str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight / (self.height ** 2), 2)

        return bmi


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.email)
    print('BMI: ', patient.bmi)
    print('Updated Successfully')

patient_info = {'name':'nitish','email': 'abc@hdfc.com', 'age': '69', 'weight' : 75.2, 'height': 1.72,'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{ 'phone':'8191980879','emergency': '453453' }}

patient1 = Patient(**patient_info)

update_patient_data(patient1)