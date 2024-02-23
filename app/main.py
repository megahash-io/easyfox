
import subprocess
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import Settings
from app.routers import home, einstufung, up

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yeld` on app shutdown.
    """

    print("Running tailwindcss...")
    try:
        subprocess.run([
            "tailwindcss",
            "-i",
            "app/static/src/tw.css",
            "-o",
            "app/static/css/main.css",
            "--minify"
        ])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    print("Done!")

    yield

def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""

    app = FastAPI(**settings.fastapi_kwargs,lifespan=lifespan)
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    app.include_router(home.router)
    app.include_router(einstufung.router)
    app.include_router(up.router)

    return app


app = get_app()


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=3999)
