#!/usr/bin/env python3
import requests
from pprint import pprint

url = "http://127.0.0.1:8080"

cliente = {"nome": "Joao Pedro", "endereco": "Rua XYZ"}

requests.post(f"{url}/cliente", json=cliente)

r = requests.get(f"{url}/cliente")
pprint(r.json())
