# user_routes.py
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from services.user_service import UserService
from models import User
from schemas.user import UserOut # type: ignore
from typing import List

user_router = APIRouter()
user_service = UserService()

templates = Jinja2Templates(directory="templates")


@user_router.get("/user_details", response_class=HTMLResponse)
async def user_details(request: Request):
    username = request.session.get("user")
    email= request.session.get("email")
    print ("details", username, email)
    return templates.TemplateResponse("user_details.html", {"request": request, 'username':username, 'email':email})



@user_router.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    username = request.session.get("user")
    email = request.session.get("email")

    return templates.TemplateResponse("profile.html", {"request": request, 'username':username, 'email':email})