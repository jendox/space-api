import random
from pathlib import Path

from fastapi import APIRouter
from starlette.responses import HTMLResponse

space_facts = [
    {"id": 1, "fact": "На Сатурне и Юпитере идут дожди из алмазов"},
    {"id": 2, "fact": "Солнечному свету требуется 8 минут 20 секунд, чтобы достичь Земли"},
    {"id": 3, "fact": "В космосе тьма, потому что нет атмосферы, которая рассеивает свет"},
    {"id": 4, "fact": "МКС - самый дорогой объект, когда-либо построенный человечеством"},
    {"id": 5, "fact": "Венера - самая горячая планета в Солнечной системе"},
]

company_info = {"company_name": "Horns and Hooves", "company_address": "Pushkin street, 12"}

router = APIRouter()


def read_html_file():
    path = Path("templates/index.html")
    with open(path, "r") as file:
        return file.read()


@router.get(
    path="/",
    description="Show main page",
    response_class=HTMLResponse,
)
async def main_page():
    return read_html_file()


@router.get(
    path="/info",
    description="Get company info"
)
async def get_info():
    return company_info


@router.get(
    path="/random-fact",
    description="Get one random fact about space"
)
async def get_random_fact():
    return random.choice(space_facts)


@router.get(
    path="/all-facts",
    description="Get all facts about space"
)
async def get_all_facts():
    return {"facts": space_facts, "count": len(space_facts), "status": "success"}
