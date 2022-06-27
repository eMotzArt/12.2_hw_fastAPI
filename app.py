from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles

from loader.views import loader_blueprint
from main_route.views import main_blueprint


app = FastAPI()
app.include_router(main_blueprint)
app.include_router(loader_blueprint, prefix="/load")

app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")



#ручка для всех uploads/images (на случай если не вмонитрована статика на папку uploads)
@app.get('/uploads/images/{path}')
async def image_getter(path):
    return FileResponse(f'uploads/images/{path}')
