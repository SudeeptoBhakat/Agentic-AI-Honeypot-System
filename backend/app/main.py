from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.v1.router import api_router
from app.core.logging import setup_logging
import os

app = FastAPI(title="HoneyPOT")

setup_logging()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# API ROUTES
# -------------------------
app.include_router(api_router, prefix="/api/v1")

# -------------------------
# ADMIN / HTML ROUTES
# -------------------------
router = APIRouter()
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "frontend", "templates")
)

# Admin route
@router.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse(
        "admin.html",
        {"request": request}
    )

# User route
@router.get("/user", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse(
        "user.html",
        {"request": request}
    )

# ✅ IMPORTANT: include the router
app.include_router(router)

# -------------------------
# STATIC FILES (LAST!)
# -------------------------
frontend_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "frontend")
)
# JS and CSS file route 
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
