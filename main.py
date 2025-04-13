from fastapi import FastAPI
import requests

app = FastAPI()

MAPBOX_API_KEY = "pk.eyJ1IjoiYWRyb2l0bmVzcyIsImEiOiJjbTlnNjNiZTUwZ2FsMmxwdDF5eTM0emE5In0.WOpDDb16X5_5pGm6n-YB5w"

@app.get("/")
def read_root():
    return {"message": "CRE Pro Forma API is live!"}

@app.get("/parcel-acreage")
def get_parcel_acreage(address: str):
    response = requests.get(f"https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={MAPBOX_API_KEY}")
    data = response.json()

    if data['features']:
        # Simple example, adjust as needed for real acreage data
        acreage = "5.0"  # Placeholder value
    else:
        acreage = "Not found"

    return {"address": address, "acreage": acreage}
