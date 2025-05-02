from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "templates"

def send_email(to: str, subject: str, template_name: str, context: dict):
    template_path = TEMPLATE_DIR / template_name

    # TODO: Agregar logica para armar template con valores del context que son las variables para el template.

    # TODO: Agregar SMTP para enviar email