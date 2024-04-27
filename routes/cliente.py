from fastapi import APIRouter
from config.db import conn
from models.cliente import clientes


cliente = APIRouter()


@cliente.get("/clientes")
def get_customers():
       return conn.execute(clientes.select()).fetchall()

@cliente.post("/clientes")
def create_customer(cliente: cliente):
        return "helloworld"

# @cliente.get("/clientes")
# def hello_world():
#        return "helloworld"

# @cliente.get("/clientes")
# def hello_world():
#        return "helloworld"

# @cliente.get("/clientes")
# def hello_world():
#        return "helloworld"