from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

# insert_data("Yoda", 800)

class User(BaseModel):
    '''A class to represent a user with various attributes and validations.'''

    name: Annotated[
        str, 
        Field(
            min_length=1, 
            max_length=50, 
            title="Name of the user", 
            description="Full name of the user"
        )
    ]
    age: Annotated[
        int, Field(
            gt=0, 
            title="Age of the user", 
            description="Age in years, must be a positive integer",
            strict=True
        )
    ]
    email: Annotated[
        EmailStr, Field(
            title="Email of the user", 
            description="Email address of the user"
        )
    ]
    weight: Annotated[
        float, Field(
            gt=0, 
            title="Weight of the user",
            description="Weight in kilograms, must be a positive number",
            strict=True
        )
    ]
    married: Annotated[
        Optional[bool], Field(
            default=False, 
            title="Marital status of the user", 
            description="Indicates if the user is married"
        )
    ]
    strength: Annotated[
        List[str], Field(
            min_items=1, 
            title="Strengths of the user", 
            description="List of strengths or skills of the user"
        )
    ]
    contacts: Annotated[
        Optional[Dict[str, EmailStr]], Field(
            default=None, title="Contacts of the user", 
            description="A dictionary of contact names and their email addresses"
        )
    ]

def insert_data(userdata: User):

    print("name: " ,userdata.name)
    print("age: " ,userdata.age)
    print("email: " ,userdata.email)
    print("weight: " ,userdata.weight)
    print("married: " ,userdata.married)
    print("strength: " ,userdata.strength)
    print("contacts: " ,userdata.contacts)
    print("Data inserted successfully")

user_info_1 = {'name': 'Yoda', 'age': 800, 'email': 'yoda@jedi.com', 'weight': 75.5, 'strength': ['Force Push', 'Lightsaber Combat'], 'contacts': {'Luke': 'luke@jedi.com', 'Leia': 'leia@jedi.com'}}
user1 = User(**user_info_1)

user_info_2 = {'name': 'Darth Vader', 'age': 45, 'email': 'darth@empire.com', 'weight': 90.0, 'strength': ['Force Choke', 'Lightsaber Combat'], 'contacts': {'Palpatine': 'palpatine@empire.com'}}
user2 = User(**user_info_2)

user_info_3 = {'name': 'Obi-Wan Kenobi', 'age': 57, 'email': 'obiwan@jedi.com', 'weight': 80.0, 'strength': ['Force Mind Trick', 'Lightsaber Combat'], 'contacts': {'Anakin': 'anakin@jedi.com', 'Padme': 'padme@jedi.com'}}
user3 = User(**user_info_3)

user_info_4 = {'name': 'Luke Skywalker', 'age': 25, 'email': 'luke@jedi.com', 'weight': 70.0, 'strength': ['Force Leap', 'Lightsaber Combat']}
user4 = User(**user_info_4)

user_info_5 = {'name': 'Anakin Skywalker', 'age': 30, 'email': 'anakin@jedi.com', 'weight': 85.0, 'married': True, 'strength': ['Force Lightning', 'Lightsaber Combat'], 'contacts': {'Padme': 'padme@jedi.com'}}
user5 = User(**user_info_5)

print("-----")
insert_data(user1)
print("-----")
insert_data(user2)
print("-----")  
insert_data(user3)
print("-----")
insert_data(user4)
print("-----")
insert_data(user5)  
print("-----")