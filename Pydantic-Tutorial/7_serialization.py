from pydantic import BaseModel
from typing import Dict, Optional

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender:str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'Chamoli','state' : 'Uttarakhand', 'pin': '246424'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Arush', 'age': 25, 'address': address1}
patient1 = Patient(**patient_dict)

temp = patient1.model_dump()  # exporting this pydantic model in the form of dictionary
# temp = patient1.model_dump(include = ['name', 'age'])  # For including specific keys
# temp = patient1.model_dump(exclude = ['name', 'age'])  ## For excludeing specific keys
temp = patient1.model_dump(exclude_unset = True)     ## For excludeing the keys which are not given during the time of object creation
print(temp)

temp2 = patient1.model_dump_json()  ## exporting this pydantic model in the form of json file
print(temp2)
print(type(temp2))