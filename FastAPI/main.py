from email.policy import default
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Path, HTTPException , Query
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import shutil

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description = 'ID of the patient', example = 'P001')]
    name : Annotated[str, Field(..., description = 'Name of the Patient', example = 'Sachin')]
    city: Annotated[str, Field(..., description = 'City of the Patient', example = 'Gopeshwar')]
    age : Annotated[int, Field(..., description = 'Age of the Patient', example = 34)]
    gender : Annotated[Literal['male', 'female', 'others'], Field(..., description = 'Gender of the Patient', example = 'Male')]
    height: Annotated[float, Field(..., description = 'Height of the Patient in meters ', example = 1.65)]
    weight : Annotated[float, Field(..., description = 'Weight of the Patient in kg', example = 70.5)]
     

    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round((self.weight/self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Good'
        else:
            return 'Obese'
     

class PatientUpdate(BaseModel):

    name : Annotated[Optional[str], Field(default = None)]
    city: Annotated[Optional[str], Field(default = None)]
    age : Annotated[Optional[int], Field(default = None, gt = 0)]
    gender : Annotated[Optional[Literal['male', 'female', 'others']], Field(default = None)]
    height: Annotated[Optional[float], Field(default = None, gt = 0)]
    weight : Annotated[Optional[float], Field(default = None, gt = 0)]
     

def load_data():
    try:
        with open('patients.json','r') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
    return data

def save_data(data):
    # Backup the file before overwriting
    try:
        shutil.copy('patients.json', 'patients_backup.json')
    except FileNotFoundError:
        pass  # No backup if file doesn't exist yet
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}


@app.get("/about")
def about():
    return {'message': 'Fully Functional API to manage your patients records'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def patient_detail(patient_id: str = Path(..., description = 'ID of the patient in the DB', example = 'P001')):
    ## load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient Not Found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = 'Sort on the basis of height , weight or bmi'), order: str = Query('asc', description = 'Sort in ascending or descending order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:  # <-- corrected logic
        raise HTTPException(status_code = 400, detail = f'Invalid field, select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 400, detail = f'Invalid order, select between asc and desc')
    
    data = load_data()
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data



@app.post('/create')
def create_patient(patient: Patient):
    
    ## Load existing data
    data = load_data()

    ## check if the patient already esists
    if patient.id in data:
        raise HTTPException(status_code = 400, detail = 'Patient already exists')

    ## new patient add to the database
    data[patient.id] = patient.model_dump(exclude = ['id'])

    ## save into the json file
    save_data(data)

    return JSONResponse(status_code = 201, content = {'message': 'patient created successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    # Update fields
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # Recalculate bmi and verdict
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    updated_dict = patient_pydantic_obj.model_dump(exclude={'id'})  # get updated dict

    # Save back to data
    data[patient_id] = updated_dict
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    #load the data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = 'Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code = 200 ,content = {'message': 'Patient deleted'})