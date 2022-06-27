from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
import os

from classes import NewPostFromRequestData, DataBase

loader_blueprint = APIRouter()
path = os.path.dirname(__file__)
templates = Jinja2Templates(directory=f"{path}/templates")


@loader_blueprint.get('/')
async def loader_page(request: Request):
    return templates.TemplateResponse("post_form.html", {"request": request})


@loader_blueprint.post('/')
async def upload(request: Request, picture: UploadFile = File(...), content: str = Form()):
    new_post = NewPostFromRequestData(picture, content)
    info_to_explore = new_post.get_info_to_export()
    new_post.save_file()

    DataBase('posts.json').append_new_post_to_db(info_to_explore)

    return templates.TemplateResponse("post_uploaded.html", {"request": request, 'post': info_to_explore})
