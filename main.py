#main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes.auth_routes import auth_router
from routes.gallery_routes import gallery_router
from routes.user_routes import user_router
from starlette.middleware.sessions import SessionMiddleware
import secrets
import string
from fastapi.staticfiles import StaticFiles
from dataclasses import dataclass


# Step 1: Generate a secret key
def generate_secret_key(length=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Use the generated secret key for session management
secret_key = generate_secret_key()

# Step 3: Create a FastAPI app
app = FastAPI()

# Step 4: Use the secret key for session management
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Initialize templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    # Here you can fetch the user information, for example from the request
    user = request.session.get("user")
    print(user)

    # Pass the user object to the template context
    return templates.TemplateResponse("home.html", {"request": request, "user": user})

# Include the authentication routes
app.include_router(auth_router)
app.include_router(gallery_router)
app.include_router(user_router)
