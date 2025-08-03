import asyncio
from itertools import count
from pathlib import Path

from fastapi import APIRouter
from starlette.responses import HTMLResponse, StreamingResponse

company_info = {"company_name": "Horns and Hooves", "company_address": "Pushkin street, 12"}

router = APIRouter()


def read_html_file():
    path = Path("templates/index.html")
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        return content.replace("{{company_name}}", company_info["company_name"]).replace(
            "{{company_address}}", company_info["company_address"]
        )


@router.get(
    path="/",
    description="Show main page",
    response_class=HTMLResponse,
)
async def main_page():
    return read_html_file()


@router.get(path="/info", description="Get company info")
async def get_info():
    return company_info


@router.get(path="/counter", description="Get endless counter")
async def get_counter():
    async def counter_generator():
        counter = count(start=1, step=1)
        while True:
            await asyncio.sleep(0.5)
            yield f"{counter.__next__()} "

    return StreamingResponse(
        counter_generator(),
        media_type="text/html",
    )
