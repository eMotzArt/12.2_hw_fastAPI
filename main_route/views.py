from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from classes import DataBase
import os

main_blueprint = APIRouter()

path = os.path.dirname(__file__)
templates = Jinja2Templates(directory=f"{path}/templates")

'''Я так понял - это бессмысленно, при импорте API роутера  импортируются только URL-ручки'''
# staticfiles = StaticFiles(directory="static")
# main_blueprint.mount("/static", staticfiles, name="static")

@main_blueprint.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@main_blueprint.get('/search')
async def search_page(request: Request, s: str):

    # Это не нужно, параметр можно прописывать прямо в функции (указывая имя поля из html'ки)
    # search_line = request.query_params.get('s')


    search_result = DataBase('posts.json').search_str_in_db_data(s)
    return templates.TemplateResponse("post_list.html", {"request": request, "search_line": s, "posts": search_result})
