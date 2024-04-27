from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DATE
from config.db import meta, engine

clientes = Table(
    "cliente",
    meta,
    Column("cliente_id", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(90)),
    Column("apellido", String(90)),
    Column("fecha_nacimiento", DATE),
    Column("telefono", Integer, unique=True),
    Column("correo_electronico", String(70), unique=True)
)

meta.create_all(engine)