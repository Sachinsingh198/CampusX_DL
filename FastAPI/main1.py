# from fastapi import FastAPI, Path, HTTPException
# import json

# app = FastAPI()

# def load_data():
#     with open('patients.json', 'r') as f:
#         data = json.load(f)

#     return data

# @app.get('/')
# def hello():
#     return {'message': 'Patient Management System API'}

# @app.get('/about')
# def about():
#     return {'message': 'An API for managing your patients records'}

# @app.get('/view')
# def view():
#     data = load_data()

#     return data

# @app.get('/patient/{patient_id}')
# def patient_detatil(patient_id: str):
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     raise HTTPException(status_code = 404, detail = 'Patient not found')

from fastapi import FastAPI,HTTPException
import json
 
app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get('/')
def Hello():
    return {'message': 'Hey I am creating my own api'}

@app.get('/about')
def about():
    return {'message': 'Introducing PaMa'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/view/{patient_id}')
def patient_details(patient_id:str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient Not found')

