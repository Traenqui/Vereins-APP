from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import yaml
import os
import logging
import logging.config

from app.api.v1.api import api_router
from app.core.config import settings

# Logging
def replace_env_for_config(log_conf: dict) -> None:
    for k, v in log_conf.items():
        if isinstance(v, dict):
            replace_env_for_config(v)
        elif isinstance(v, str) and v[0] == '$':
            log_conf[k] = os.environ.get(v[1:])

def create_log_config(log_path: str) -> dict:
    with open(log_path, 'r') as f:
        log_config = yaml.load(f, Loader=yaml.CLoader)
        replace_env_for_config(log_config)
    return log_config

log_config = create_log_config('app/conf/logging.yaml')
logging.config.dictConfig(log_config)

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/docs",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)