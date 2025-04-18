from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import re

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, user_input: str = Form(...)):
    if not re.fullmatch(r"[A-Za-z]+", user_input):
        result = "Ошибка: допустимы только латинские буквы (A-Z, a-z)."
    else:
        result = " ".join(str(ord(c.upper()) - 64) for c in user_input)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
