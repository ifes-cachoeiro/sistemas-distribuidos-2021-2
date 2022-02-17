#!/usr/bin/env python3
import requests
from pprint import pprint

url = "http://127.0.0.1:8080"

clientes = [
    {"nome": "Amanda", "endereco": "Rua 456"},
    {"nome": "Carolina", "endereco": "Rua asd"},
    {"nome": "Daniel", "endereco": "Rua dfg"},
    {"nome": "Viviane", "endereco": "Rua 4d"},
    {"nome": "Theo", "endereco": "Rua dfgg6"},
    {"nome": "Ricardo", "endereco": "Rua dfgg"},
    {"nome": "Antonio", "endereco": "Rua dfggd"}
]

for cliente in clientes:  
    requests.post(f"{url}/cliente", json=cliente)

r = requests.get(f"{url}/cliente")
pprint(r.json())
