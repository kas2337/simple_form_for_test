from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from alpabet import get_letter_number, is_substr_in_alphabet

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, user_input: str = Form(...)):
    status_code = 200
    result = f"{get_letter_number(user_input[0])}"
    if not is_substr_in_alphabet(user_input):
        if user_input.isdigit():
            status_code = 400
        else:
            status_code = 500
    return templates.TemplateResponse("index.html", {"request": request, "result": result, "user_input": user_input}, status_code)
