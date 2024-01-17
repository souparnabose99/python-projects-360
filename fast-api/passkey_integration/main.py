from typing import List
from corbado_python_sdk.entities.session_validation_result import (
    SessionValidationResult,
)
from corbado_python_sdk.generated.models.identifier import Identifier
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from corbado_python_sdk import (
    Config,
    CorbadoSDK,
    IdentifierInterface,
    SessionInterface,
)

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

PROJECT_ID: str = os.getenv("PROJECT_ID", "pro-xxx")
API_SECRET: str = os.getenv("API_SECRET", "corbado1_xxx")

# Session config
short_session_cookie_name = "cbo_short_session"

# Config has a default values for 'short_session_cookie_name' and 'BACKEND_API'
config: Config = Config(
    api_secret=API_SECRET,
    project_id=PROJECT_ID,
)

# Initialize SDK
sdk: CorbadoSDK = CorbadoSDK(config=config)
sessions: SessionInterface = sdk.sessions
identifiers: IdentifierInterface = sdk.identifiers


@app.get("/", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse(
        "login.html", {"request": request, "PROJECT_ID": PROJECT_ID}
    )

if __name__ == "__main__":
    pass

