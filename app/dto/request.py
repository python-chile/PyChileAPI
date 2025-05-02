from pydantic import BaseModel, EmailStr

class SponsorRequest(BaseModel):
    companyName: str
    contactName: str
    email: EmailStr
    phone: str
    sponsorLevel: str
    message: str

class RegistrationRequest(BaseModel):
    name: str
    email: EmailStr
    role: str
    sendCFP: bool
    city: str
    idType: str
    idNumber: str

    # TODO: Falta agregar validaciones