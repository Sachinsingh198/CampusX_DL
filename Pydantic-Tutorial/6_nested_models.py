from pydantic import BaseModel
from typing import Dict

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Chamoli','state' : 'Uttarakhand', 'pin': '246424'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Arush', 'gender': 'male', 'age': 25, 'address': address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)