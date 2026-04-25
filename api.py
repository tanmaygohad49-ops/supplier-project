from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API working ✔"}

@app.get("/products")
def products():
    return {
        "status": "success",
        "data": [
            {"id": 1, "name": "LED Bulb", "price": 50},
            {"id": 2, "name": "Switch", "price": 30}
        ]
    }