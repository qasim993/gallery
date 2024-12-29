# pydantic_models.py

from pydantic import BaseModel
from dataclasses import dataclass
from fastapi import FastAPI, Form, Depends, UploadFile


class UserCreate(BaseModel):
    username: str
    email: str
    dob: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str


class CreateGallery(BaseModel):
    username: str
    content: str
    image: UploadFile


class EditGallery(BaseModel):
    username: str
    content: str
    image: UploadFile