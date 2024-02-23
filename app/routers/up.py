
from fastapi import Request, APIRouter
from app.config import Settings
from jinja2_fragments.fastapi import Jinja2Blocks

settings = Settings()
templates = Jinja2Blocks(directory=settings.TEMPLATE_DIR)

router = APIRouter()

@router.get("/up",status_code=200)
def up(request: Request):
    """Home page - generates an image and name of a random artist."""

    return ""
