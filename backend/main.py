from fastapi import FastAPI, HTTPException, Request
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from routes import vendor, product, purchase_order
from auth import create_access_token

# 🔥 Google Auth imports
from google.oauth2 import id_token
from google.auth.transport import requests

# CREATE TABLES
models.Base.metadata.create_all(bind=engine)

# INIT APP
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
app.include_router(vendor.router, prefix="/vendors", tags=["Vendors"])
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(purchase_order.router, prefix="/po", tags=["Purchase Orders"])


# 🔐 BASIC LOGIN (manual)
@app.post("/login")
def login(username: str, password: str):

    if username != "admin" or password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# 🔥 GOOGLE LOGIN
@app.post("/google-login")
async def google_login(request: Request):

    body = await request.json()
    token = body.get("token")

    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            "1011978382585-9etr8sas1442da7rpnas4iqbcgg6cqbo.apps.googleusercontent.com"   # ⚠️ REPLACE THIS
        )

        email = idinfo["email"]

        # create your own JWT
        access_token = create_access_token({"sub": email})

        return {"access_token": access_token}

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Google token")
