# auth_routes.py

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic_models import UserCreate, UserLogin
from controllers.auth_controller import AuthController
from services.auth_service import AuthService

auth_router = APIRouter()
templates = Jinja2Templates(directory="templates")

auth_service = AuthService()
auth_controller = AuthController(auth_service)

@auth_router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    # Here you can fetch the user information, for example from the request
    user = request.session.get("user")
    print ("home", user)
    # Pass the user object to the template context
    return templates.TemplateResponse("home.html", {"request": request, "user": user})


@auth_router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth_router.post("/login", response_class=HTMLResponse)
async def login(request: Request, user: UserLogin):
    try:
        authenticated_user=auth_controller.login_user(user.email, user.password)
        # Store user data in session
        request.session["user"] = authenticated_user['user']
        request.session["email"]=user.email
        print("Login successful. Redirecting to home page...")
        # Redirect to the home page (root page) after successful login
        return RedirectResponse("/home", status_code=303)
    except HTTPException as e:
        return templates.TemplateResponse("login.html", {"request": request, "error_message": e.detail})


@auth_router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@auth_router.post("/register", response_class=HTMLResponse)
async def register(request: Request, user: UserCreate):
    try:
        auth_controller.register_user(user.username, user.email, user.dob, user.password)
        print("Registration successful. Redirecting to login page...")
        # Redirect to the login page after successful registration
        return RedirectResponse("/login", status_code=303)
    except HTTPException as e:
        print(f"Registration failed: {e}")
        return templates.TemplateResponse("register.html", {"request": request, "error_message": e.detail})
    
@auth_router.get("/logout")
async def logout(request: Request):
    # Clear session data to logout user
    request.session.clear()
    # Redirect user to the login page or any other page you prefer
    return RedirectResponse(url="/login")