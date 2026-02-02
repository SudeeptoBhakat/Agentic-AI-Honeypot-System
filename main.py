from pathlib import Path
from fastapi import FastAPI, Request
# import whisper
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
# model = whisper.load_model("base")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# @app.post("/upload-audio/")
# async def upload_audio(file: UploadFile = File(...)):
#     with open(file.filename, "wb") as f:
#         f.write(await file.read())
#     result = model.transcribe(file.filename)
#     text = result["text"]
#     return {"transcript": text}
        
        # jit aiml branch working