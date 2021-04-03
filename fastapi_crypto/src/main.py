from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import symmetric_view, asymmetric_view, home_view


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(home_view.router)
app.include_router(symmetric_view.router)
app.include_router(asymmetric_view.router)

