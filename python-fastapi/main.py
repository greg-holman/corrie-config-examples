"""Minimal FastAPI app that reads its settings from environment variables.

Start it with the Corrie Config launcher so the variables come from config.corrie.io:
    CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- uvicorn main:app --port 8000
"""
import os

from fastapi import FastAPI

SETTINGS = {
    "api_url": os.environ.get("API_URL", ""),
    "new_checkout": os.environ.get("FEATURE_NEW_CHECKOUT") == "true",
    "db_host": os.environ.get("DB_HOST", ""),
    "db_pool": int(os.environ.get("DB_POOL", "5")),
}

app = FastAPI()


@app.get("/")
def index():
    return {"ok": True, "settings": SETTINGS}
