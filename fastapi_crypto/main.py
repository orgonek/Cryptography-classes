from fastapi import FastAPI
from routers import symmetric_view, asymmetric_view, home_view
import uvicorn

app = FastAPI()

app.include_router(home_view.router)
app.include_router(symmetric_view.router)
app.include_router(asymmetric_view.router)

