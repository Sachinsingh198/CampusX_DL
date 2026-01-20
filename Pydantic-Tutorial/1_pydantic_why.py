
from multiprocessing import Value


def insert_patient_data(name : str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise Value('Age cannot be negative')
        else:
            print(name)
            print(age)
            print('Inserted Successfully')
    else:
        raise TypeError('Incorrect Datatype')
## database is expecting us to pass the integer value to the function at the age, but still this program gets executed successfully , and the database gets the wrong value, it is a failure of the pyhton, because here the type validation is not supported

insert_patient_data('Sachin','daf')

