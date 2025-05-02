from fastapi import APIRouter
from dto.request import SponsorRequest, RegistrationRequest

router = APIRouter()

@router.post("/sponsors")
def sponsor_email(request: SponsorRequest) -> str:
    # TODO Logear y guardar datos en DB(?) de sponsor.
    return "Sponsor saved"

@router.post("/registration")
def registration_email(request: RegistrationRequest) -> str:
    # TODO: Logear, generar template y enviar correo con ticket.
    return "Ticket sent"
