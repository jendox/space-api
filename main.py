from fastapi import FastAPI

from api import router

app = FastAPI(title="SpaceAPI", version="0.1", description="Find out interesting facts about space")

app.include_router(router=router)
