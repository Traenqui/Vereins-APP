from uuid import UUID
from datetime import date
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    table_name = __name__

    id: UUID                # uuid
    user_id: str            # 
    is_active: bool = True
    is_superuser: bool = False

    # details 
    salutation: str         # Herr / Frau
    address: str            # Lieber, sehr geehrter 
    surname: str            # Vorname
    second_name: str        # Zweitname
    lastname: str           # Nachname
    gender: str
    civil_status: str
    date_of_birth: date
    nationality: str

    # adress 1
    street1: str
    street_number1: str
    plz1: str
    city1: str
    country1: str

    # address 2
    street2: str
    street_number2: str
    plz2: str
    city2: str
    country2: str

    # contact inforamtion
    phone_private: str
    phone_mobile: str
    phone_work: str
    fax: str
    email_private: EmailStr
    email_work: EmailStr

    # information association
    signing_entry_form: date                        # Datum der 10er Note
    entry_association: date                         # Aufnahme Verbindung
    entry_umbrella_association: date                # Aufnahme Schw. StV
    status: str                                     # Fux, Bursch, Altherr, Interessent
    department: list                                # Revisor, Senior Fuchsmajor etc..
    vulgo: str
    group: list                                     # AC, BC, FC, Komitee, Kommisionen
    
    # Beerfamily
    biervater: str                                  # Biervater
    biersoehne: list                                # Biersöhne

class UserIn(User):
    password: str

class UserOut(User):
    pass

class UserInDB(User):
    hashed_password: str