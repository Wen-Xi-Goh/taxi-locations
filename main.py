import requests
import json
import folium
from pyodide.ffi import JsProxy
def get_taxi_json(event=None):
    response = requests.get("https://raw.githubusercontent.com/Wen-Xi-Goh/taxi-locations/refs/heads/main/taxi-data.json")
    get_taxi_dict(response.text)
    return response.text
def get_taxi_dict(jsonText = None):
    if jsonText==None:
        jsonText=get_taxi_json()
    # Convert the JsProxy object to a Python string
    #print("Content of jsonText:", jsonText)
    responsedict=json.loads(jsonText)
    print(responsedict)
