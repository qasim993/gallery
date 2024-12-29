from fastapi import APIRouter, Request, Body, Depends, Form, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic_models import CreateGallery
from dataclasses import dataclass

from controllers.gallery_controller import GalleryController

gallery_router = APIRouter()
templates = Jinja2Templates(directory="templates")

gallery_controller = GalleryController()

@gallery_router.get("/create/{user_name}", response_class=HTMLResponse)
async def create_gallery_page(request: Request, user_name: str):
    return templates.TemplateResponse("createGallery.html", {"request": request,"user": user_name})

@gallery_router.post("/create/{user_name}", response_class=HTMLResponse)
async def create_gallery(request: Request,
                         user_name: str ,
                         gallery_name: str = Form(...),
                         gallery_image: UploadFile = Form(...),):
    # Validate form data, save the image, and handle business logic
    print(f"User Name: {user_name}")
    print(f"Gallery Name: {gallery_name}")
    print(f"Image Filename: {gallery_image.filename}")
    gallery_controller.create_gallery(user_name, gallery_name, gallery_image)
    return templates.TemplateResponse("createGallery.html",
                                      {"request": request,
                                       "success_message": "Gallery created successfully"})


@gallery_router.get("/view/{user_name}", response_class=HTMLResponse)
async def view_gallery(request: Request, user_name: str):
    gallery_docs = gallery_controller.view_gallery(user_name)
    return templates.TemplateResponse("view.html", {"request": request,"user": user_name,
                                                    "gallery_docs":gallery_docs})
"""


@gallery_router.post("/view/{user_name}", response_class=HTMLResponse)
async def view_gallery_page(request: Request, user_name: str):
    gallery_docs = gallery_controller.view_gallery(user_name)
    return templates.TemplateResponse("view.html", {"request": request, "gallery_docs":gallery_docs})
"""


@gallery_router.get("/edit_gallery/{gallery_id}", response_class=HTMLResponse)
async def edit_gallery_page(request: Request, gallery_id: int):
    gallery = gallery_controller.get_gallery(gallery_id)
    return templates.TemplateResponse("edit.html", {"request": request, "gallery edit": gallery})

@gallery_router.post("/edit_gallery/{gallery_id}", response_class=HTMLResponse)
async def edit_gallery(request: Request, gallery_id: int, gallery_data: CreateGallery):
    gallery_controller.edit_gallery(gallery_id, gallery_data.content)
    return templates.TemplateResponse("edit.html", {"request": request, "success_message": "Gallery edited successfully"})


@gallery_router.post("/delete_gallery/{gallery_id}", response_class=HTMLResponse)
async def delete_gallery(request: Request, gallery_id: int):
    gallery_controller.delete_gallery(gallery_id)
    return templates.TemplateResponse("delete_gallery.html", {"request": request, "success_message": "Gallery deleted successfully"})

