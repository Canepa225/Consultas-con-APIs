import requests
import json
import pandas as pd

response = requests.get("https://rickandmortyapi.com/api/character").text
jsonResponse = json.loads(response)
#print(jsonResponse)

pdObjeto = pd.DataFrame(jsonResponse["results"])
print(pdObjeto)                         
pdObjeto.to_csv("rickandmorty.csv")