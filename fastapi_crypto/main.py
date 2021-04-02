from fastapi import FastAPI
from routers import symmetric, asymmetric


app = FastAPI()


app.include_router(symmetric.router)
app.include_router(asymmetric.router)


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Main page"}


