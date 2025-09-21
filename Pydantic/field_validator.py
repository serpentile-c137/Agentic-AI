from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    phone: Optional[str] = None
    symptoms: List[str]
    medical_history: Optional[List[str]] = None
    allergies: Optional[List[str]] = None
    contact_info: Dict[str, str] = None

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['icici.com', 'hdfc.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Email must be from the domain icici.com or hdfc.com')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


def insert_data(patient: Patient):

    print('name: ', patient.name)
    print('age: ', patient.age)
    print('email: ', patient.email)
    print('phone: ', patient.phone)
    print('symptoms: ', patient.symptoms)
    print('medical_history: ', patient.medical_history)
    print('allergies: ', patient.allergies)
    print('contact_info: ', patient.contact_info)
    print('Inserting data into the database...')

    


patient_info_1 = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@icici.com',
    'phone': '123-456-7890',
    'symptoms': ['cough', 'fever'],
    'medical_history': ['asthma'],
    'allergies': ['penicillin'],
    'contact_info': {'emergency_contact': 'Jane Doe'}
}

p1 = Patient(**patient_info_1)
# insert_data(p1)

patient_info_2 = {
    'name': 'Alice Smith',
    'age': 25,
    'email': 'alice.smith@hdfc.com',
    'symptoms': ['headache'],
    'contact_info': {'emergency_contact': 'Bob Smith'}
}

p2 = Patient(**patient_info_2)
# insert_data(p2)

print('------')
insert_data(p1)
print('------')
insert_data(p2)