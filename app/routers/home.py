
from fastapi import Request, APIRouter
from app.config import Settings
from jinja2_fragments.fastapi import Jinja2Blocks

settings = Settings()
templates = Jinja2Blocks(directory=settings.TEMPLATE_DIR)

router = APIRouter()

@router.get("/")
def home(request: Request):
    """Home page - generates an image and name of a random artist."""

    return templates.TemplateResponse( "home.html", { "request": request } )
