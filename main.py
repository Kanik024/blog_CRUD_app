from fastapi import FastAPI
from app.routes.routes import router as app_router  # Import the router from routes module

app = FastAPI()
app.include_router(app_router)  # Include the router in the FastAPI app