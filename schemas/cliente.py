from pydantic import BaseModel
from typing import Optional
from datetime import date


class cliente (BaseModel):
        cliente_id:Optional[str]
        nombre: str
        apellido: str
        fecha_nacimiento: date
        telefono: str
        email: str

